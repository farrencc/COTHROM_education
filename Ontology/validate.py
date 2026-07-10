#!/usr/bin/env python3
"""Validate the COTHROM ontology and derive a teaching order.

Loads Ontology/concepts.csv and Ontology/relationships.csv and:

1. checks every edge references a valid concept id (and that ids are unique,
   enum fields are in range, and no edge is an exact duplicate);
2. checks the *hard* ``prerequisite_for`` subgraph is acyclic, printing any
   cycle found;
3. assigns each concept a learning "layer" = its longest hard-prerequisite
   depth (roots are layer 0);
4. emits Ontology/teaching_order.csv, concepts sorted by layer then tier.

It also prints every cross-tier hard prerequisite edge, which feeds
REVIEW.md. Exits non-zero on any validation failure so it can run in CI.

Usage:  python Ontology/validate.py
"""

import csv
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONCEPTS_CSV = HERE / "concepts.csv"
RELATIONSHIPS_CSV = HERE / "relationships.csv"
TEACHING_ORDER_CSV = HERE / "teaching_order.csv"

TIERS = [
    "background_electoral",
    "data",
    "metric",
    "physics_model",
    "algorithm",
    "decision_analysis",
    "meaning",
]
KINDS = {"definition", "metric", "method", "principle", "object", "analogy"}
RELATIONS = {
    "prerequisite_for",
    "part_of",
    "formalises",
    "motivates",
    "in_tension_with",
    "analogy_for",
    "contrasts_with",
}
STRENGTHS = {"hard", "soft"}
CONFIDENCES = {"high", "medium", "low"}


def load_concepts():
    errors = []
    concepts = {}
    with CONCEPTS_CSV.open(newline="", encoding="utf-8") as f:
        for i, row in enumerate(csv.DictReader(f), start=2):
            cid = row["id"].strip()
            if not cid:
                errors.append(f"concepts.csv line {i}: empty id")
                continue
            if cid in concepts:
                errors.append(f"concepts.csv line {i}: duplicate id '{cid}'")
            if row["tier"] not in TIERS:
                errors.append(f"concepts.csv '{cid}': bad tier '{row['tier']}'")
            if row["kind"] not in KINDS:
                errors.append(f"concepts.csv '{cid}': bad kind '{row['kind']}'")
            if row["confidence"] not in CONFIDENCES:
                errors.append(
                    f"concepts.csv '{cid}': bad confidence '{row['confidence']}'"
                )
            try:
                if not 1 <= int(row["difficulty"]) <= 5:
                    raise ValueError
            except ValueError:
                errors.append(
                    f"concepts.csv '{cid}': difficulty '{row['difficulty']}' not in 1-5"
                )
            concepts[cid] = row
    return concepts, errors


def load_relationships(concepts):
    errors = []
    edges = []
    seen = set()
    with RELATIONSHIPS_CSV.open(newline="", encoding="utf-8") as f:
        for i, row in enumerate(csv.DictReader(f), start=2):
            src, tgt = row["source_id"].strip(), row["target_id"].strip()
            for cid in (src, tgt):
                if cid not in concepts:
                    errors.append(
                        f"relationships.csv line {i}: unknown concept id '{cid}'"
                    )
            if row["relation"] not in RELATIONS:
                errors.append(
                    f"relationships.csv line {i}: bad relation '{row['relation']}'"
                )
            if row["strength"] not in STRENGTHS:
                errors.append(
                    f"relationships.csv line {i}: bad strength '{row['strength']}'"
                )
            if row["confidence"] not in CONFIDENCES:
                errors.append(
                    f"relationships.csv line {i}: bad confidence '{row['confidence']}'"
                )
            if src == tgt:
                errors.append(f"relationships.csv line {i}: self-loop on '{src}'")
            key = (src, tgt, row["relation"])
            if key in seen:
                errors.append(f"relationships.csv line {i}: duplicate edge {key}")
            seen.add(key)
            edges.append(row)
    return edges, errors


def hard_prereq_graph(edges):
    """adjacency: prerequisite -> set of concepts it unlocks (hard edges only)."""
    graph = {}
    for e in edges:
        if e["relation"] == "prerequisite_for" and e["strength"] == "hard":
            graph.setdefault(e["source_id"], set()).add(e["target_id"])
    return graph


def find_cycle(graph, nodes):
    """Return one cycle as a list of ids, or None. Iterative DFS with colours."""
    WHITE, GREY, BLACK = 0, 1, 2
    colour = {n: WHITE for n in nodes}
    parent = {}
    for start in nodes:
        if colour[start] != WHITE:
            continue
        stack = [(start, iter(sorted(graph.get(start, ()))))]
        colour[start] = GREY
        while stack:
            node, it = stack[-1]
            advanced = False
            for nxt in it:
                if colour[nxt] == WHITE:
                    colour[nxt] = GREY
                    parent[nxt] = node
                    stack.append((nxt, iter(sorted(graph.get(nxt, ())))))
                    advanced = True
                    break
                if colour[nxt] == GREY:  # back-edge: reconstruct the cycle
                    cycle = [nxt, node]
                    cur = node
                    while cur != nxt:
                        cur = parent[cur]
                        cycle.append(cur)
                    cycle.reverse()
                    return cycle
            if not advanced:
                colour[node] = BLACK
                stack.pop()
    return None


def assign_layers(graph, nodes):
    """layer(c) = longest chain of hard prerequisites ending at c (roots = 0)."""
    indeg = {n: 0 for n in nodes}
    for src, tgts in graph.items():
        for t in tgts:
            indeg[t] += 1
    layer = {n: 0 for n in nodes}
    queue = [n for n in nodes if indeg[n] == 0]
    processed = 0
    while queue:
        node = queue.pop()
        processed += 1
        for t in sorted(graph.get(node, ())):
            layer[t] = max(layer[t], layer[node] + 1)
            indeg[t] -= 1
            if indeg[t] == 0:
                queue.append(t)
    assert processed == len(nodes), "layer assignment ran on a cyclic graph"
    return layer


def main():
    concepts, errors = load_concepts()
    edges, rel_errors = load_relationships(concepts)
    errors += rel_errors
    if errors:
        print(f"FAIL: {len(errors)} validation error(s):")
        for e in errors:
            print(f"  - {e}")
        return 1

    graph = hard_prereq_graph(edges)
    cycle = find_cycle(graph, concepts.keys())
    if cycle:
        print("FAIL: hard prerequisite_for subgraph has a cycle:")
        print("  " + " -> ".join(cycle))
        return 1

    layer = assign_layers(graph, concepts.keys())

    tier_rank = {t: i for i, t in enumerate(TIERS)}
    ordered = sorted(
        concepts.values(),
        key=lambda c: (layer[c["id"]], tier_rank[c["tier"]], c["id"]),
    )
    with TEACHING_ORDER_CSV.open("w", newline="", encoding="utf-8") as f:
        # lineterminator: keep LF endings, as enforced repo-wide by .gitattributes
        w = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator="\n")
        w.writerow(["layer", "tier", "id", "label", "difficulty"])
        for c in ordered:
            w.writerow([layer[c["id"]], c["tier"], c["id"], c["label"], c["difficulty"]])

    n_hard = sum(len(v) for v in graph.values())
    print(f"OK: {len(concepts)} concepts, {len(edges)} edges "
          f"({n_hard} hard prerequisites), no cycles.")
    print(f"Layers: 0..{max(layer.values())}; "
          f"teaching order written to {TEACHING_ORDER_CSV.name}.")

    cross = [
        e for e in edges
        if e["relation"] == "prerequisite_for" and e["strength"] == "hard"
        and concepts[e["source_id"]]["tier"] != concepts[e["target_id"]]["tier"]
    ]
    print(f"\nCross-tier hard prerequisites ({len(cross)}) - review these first:")
    for e in sorted(cross, key=lambda e: (tier_rank[concepts[e['source_id']]['tier']],
                                          e["source_id"], e["target_id"])):
        st = concepts[e["source_id"]]["tier"]
        tt = concepts[e["target_id"]]["tier"]
        print(f"  {e['source_id']} ({st}) -> {e['target_id']} ({tt})")

    low_conf_c = [c["id"] for c in concepts.values() if c["confidence"] != "high"]
    low_conf_e = [(e["source_id"], e["target_id"], e["relation"])
                  for e in edges if e["confidence"] != "high"]
    ext = [c["id"] for c in concepts.values() if c["paper_ref"].strip() == "external"]
    print(f"\nConcepts with confidence < high ({len(low_conf_c)}): "
          + ", ".join(sorted(low_conf_c)))
    print(f"Edges with confidence < high ({len(low_conf_e)}):")
    for s, t, r in low_conf_e:
        print(f"  {s} -{r}-> {t}")
    print(f"paper_ref=external concepts ({len(ext)}): " + ", ".join(sorted(ext)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
