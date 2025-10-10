# Installing python
## Pyenv

- Link to check pyenv to enforce correct version of python to be used in projects: https://github.com/pyenv/pyenv?tab=readme-ov-file

- install python with pyenv
```bash
pyenv install 3.12
```

- set global python
```bash
pyenv global 3.12.1
```

- set local python in project1 directory
```bash
mkdir project1
cd project1
pyenv local 3.12.1
```
-- check which python is being used in project1 = 3.12.1
```bash
cd project1
pyenv --version
```

## Pip + Venv

- uninstall all packages via pip
```bash
pip freeze | grep -v "^-e" | xargs pip uninstall -y
```

- create virtual environment with venv
```bash
python -m venv .venv
```

- activate virtual environment
```bash
source .venv/Scripts/activate
```

- deactivate virtual environment
```bash
deactivate
```

- install package called pandas
```bash
pip install pandas
```

- remove directory and all contents
```bash
rm -r directory_name
```

## pipX

- install pipx globally
```bash
pip install pipx
```

- poetry and ipython are used in all projects
```bash
pipx install poetry ipython
```

## Poetry

- install poetry globaly
```bash
pip install poetry
```

- handle virtual environments to poetry
```bash
poetry config virtualenvs.in-project true
```

- create project_name, tests folders and pyproject.toml file
```bash
poetry new project_name
```

- create virtual environment .venv
```bash
poetry env use 3.12.1
```

- add packages
```bash
poetry add django pandas streamlit
```

- remove packages
```bash
poetry remove django
```


# Notes

- dynamic types: can change variable from integer to string, etc. Python doesn't enforce a type