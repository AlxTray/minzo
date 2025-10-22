# minzo
A personal finance dashboard

# development setup
Must have Nx, Poetry, and pre-commit installed globally.

Run 'pre-commit install' to set up git hooks.

To install dependencies they need to be installed for Nx and the Python backend services.
Run 'npm install' at the root of the project for Nx.
Run 'poetry install --sync --all-extras --with dev,test,coverage' inside the services directory for Python.

## minzo website
To start the minzo frontend run 'npx nx serve minzo'.

## minzo api
To start the minzo backend run 'poetry run minzo'
