with import <nixpkgs> { config = { allowUnfree = true; }; };

let
  pythonPackages = python3Packages;
  


  sphinxcontrib-mermaid = pythonPackages.buildPythonPackage rec {
    pname = "sphinxcontrib-mermaid";
    version = "0.7.1";
    pyproject = true;
    build-system = [ pythonPackages.setuptools ];
    src = pythonPackages.fetchPypi {
      inherit pname version;
      sha256 = "sha256-qopAtQ7IatEoJLYhgCQMpSqb2oQkRV1+slLq6apdKTw=";
    };
    propagatedBuildInputs = with pythonPackages; [ sphinx ];
    pythonImportsCheck = [ "sphinxcontrib.mermaid" ];
  };

  sphinxcontrib-drawio = pythonPackages.buildPythonPackage rec {
    pname = "sphinxcontrib-drawio";
    version = "0.0.17";
    format = "setuptools";
    
    src = pythonPackages.fetchPypi {
      inherit pname version;
      sha256 = "1a3f82efd1ab4b41d1ee8dd27c296bae0944a10faca3568c462dc6b9a77748f5";
    };
    propagatedBuildInputs = with pythonPackages; [ sphinx ];
    pythonImportsCheck = [ "sphinxcontrib.drawio" ];
    
    meta = with lib; {
      description = "Sphinx extension for drawing images using drawio/diagrams.net";
      homepage = "https://github.com/mikitex70/sphinx-drawio";
    };
  };

#  jupyterlite-sphinx = pythonPackages.buildPythonPackage rec {
#    pname = "jupyterlite_sphinx";
#    version = "0.19.1";
#    src = pythonPackages.fetchPypi {
#      inherit pname version;
#      sha256 = "758941390e5f53fc635bcda9d95a1dcd77cdd3268b91fe687c55d51790b02ffe";
#    };
#    propagatedBuildInputs = with pythonPackages; [ sphinx ];
#    pythonImportsCheck = [ "jupyterlite-sphinx" ];
#  };

jupyterlite-sphinx = pythonPackages.buildPythonPackage rec {
    pname = "jupyterlite-sphinx";
    version = "0.19.1";
    format = "pyproject";  # Important for pyproject.toml based packages
    
    src = pythonPackages.fetchPypi {
      pname = "jupyterlite_sphinx";  # Note the underscore in PyPI package name
      inherit version;
      sha256 = "758941390e5f53fc635bcda9d95a1dcd77cdd3268b91fe687c55d51790b02ffe";
    };
    
    nativeBuildInputs = with pythonPackages; [
      # Build system requirements
      hatchling
      hatch-nodejs-version
      pip
      jupyter-packaging
      setuptools
      wheel
    ];
    
    propagatedBuildInputs = with pythonPackages; [
      # Runtime dependencies
      sphinx
      jupyter-sphinx
      ipython
      nbformat
      pytest
    ];
    
    # Sometimes needed to bypass version detection issues
    SETUPTOOLS_SCM_PRETEND_VERSION = version;
    
    # Disable tests to avoid build issues
    doCheck = false;
    
    pythonImportsCheck = [ "jupyterlite_sphinx" ];
    
    meta = with lib; {
      description = "JupyterLite Sphinx Extension";
      homepage = "https://github.com/jupyterlite/jupyterlite-sphinx";
    };
  };

  # Custom jupyter-book build with tests disabled
  jupyter-book-custom = pythonPackages.jupyter-book.overridePythonAttrs (old: {
    doCheck = false;
    doInstallCheck = false;
    checkPhase = "true";
    installCheckPhase = "true";
  });

in
pkgs.mkShell {
  buildInputs = with pkgs; [
    xorg.libX11
    libGL
    gcc
    cmake
    gfortran
    gsl
    doxygen
    pkgs.texlive.combined.scheme-full
    pkgs.biber
    sfml
    eigen
    fmt
    drawio
    nodejs 
    # Create a single Python environment with all required packages
    (python3.withPackages(ps: with ps; [
      # Core Python packages
      jupyter
      jupyter-book-custom  # Use custom build with tests disabled
      ipykernel
      numpy
      matplotlib
      scipy
      pandas
      sympy
      
      # Sphinx and extensions
      sphinx
      sphinxcontrib-programoutput
      # Custom packages defined above
      sphinxcontrib-mermaid
      sphinxcontrib-drawio
      # Note: sphinxcontrib-youtube removed due to incompatibility with Sphinx 8.x
    ]))
  ];

  shellHook = ''
    echo 'This shell.nix file has been made for use in The Problem Solving Association C.L.G. COTHROM project.'
    # Add this to verify the Python environment is set up correctly
    python -c "import sys; print('Python path:', sys.path)"
    python -c "import sphinx; print('Sphinx version:', sphinx.__version__)"
    python -c "import sphinxcontrib.mermaid; print('Mermaid extension found')" || echo "Mermaid extension not found"
    python -c "import sphinxcontrib.drawio; print('Drawio extension found')" || echo "Drawio extension not found"
    echo "Note: sphinxcontrib-youtube was removed due to incompatibility with Sphinx 8.x"
  '';
}
