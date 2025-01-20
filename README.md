# Purpose

Template repository used in a comparative analysis of Development Environment Management (DEM) tools such as coder, eclipse che and cloud based solutions. The repo is used to deploy a simple devcontainer including the automated configuration of vscode extensions as well as dependency installation using requirements.txt.  

For local development purposes, defining the desired extensions in the devcontainer-file is sufficient (which makes .vscode obsolete for this specific use case). In coder, the VSCode marketplace cannot be accessed due to licensing issues. Using an environment variable, the marketplace target url can be redirected to a self hosted code-marketplace (or any public vsix marketplace for that matter).  
