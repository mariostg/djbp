# My django boilerplate

## Features

- django upgrade https://github.com/adamchainz/django-upgrade
  upgrades Django code to the latest features
- pre-commit hooks
  - trailing-whitespace
  - end-of-file-fixer
  - check-yaml
  - check-added-large-files
  - detect-private-key
  - check-merge-conflict
  - check-docstring-first
  - check-executables-have-shebangs
  - check-toml
  - detect-private-key
  - requirements-txt-fixer
- flake8
  - [flake8-bugbear](https://pypi.org/project/flake8-bugbear/). A plugin for flake8 finding likely bugs and design problems in your program
  - [flake8-no-pep420](https://pypi.org/project/flake8-no-pep420/). Ban PEP-420 implicit namespace packages
  - [flake8-comprehensions](https://pypi.org/project/flake8-comprehensions/). Helps you write better list/set/dict comprehensions.
  - [flake8-print](https://pypi.org/project/flake8-print/). Check for Print statements in python files.
  - [flake8-logging](https://pypi.org/project/flake8-logging/). Checks for issues using the standard library logging module.
- [DjHTML](https://github.com/rtts/djhtml). Template indenter for html, css and js files
- Use pip-lock (manage.py) to check if requirements are up to date.
- Use django-debug-toolbar and django-browser-reload.
- Use [rich](https://rich.readthedocs.io/en/stable/). Prettify terminal output.

## Setup environment

- Virtual environment setup in .venv folder. Adjust .gitignore as necessary.
- pip-tools can be installed either in virtual environment or system wide.
- Place top-level dependencies in file called **requirements.in** with or without version constraints.
- To remove a top-level dependency, remove the dependency from **requirements.in** and run pip-compile.
- Running pip-compile will generate **requirements.txt** file. If a file already exists, consider backing up file first and run diff to compare both versions after having executed pip-compile.
- Create a .env file. Use .env-exemple to get started.
- Apply migrate
- Set up gunicorn socket
- Set up gunicofn service
- Set up Nginx

### Sequence of commands

```bash
  python -m venv .venv
  source .venv/bin/activate
  python -m pip install pip-tools
  cp requirements.txt requirements.txt.bak
  pip-compile
  diff requirements.txt requirements.txt.bak #(Not required when seeting-up for first time)
  rm requirements.txt.bak #if all is good.
  pip-sync --ask
  cp .env-exemple .env #Edit as needed
  pythmon manage.py migrate
```

## Setup project

There is no need to execute command **django-admin startproject <your project name>'**. A project has already been created and it's called **main**.

Additionally, skip the command **django-admin startapp**. App project has been created.

### Setup manage.py

```bash
diff manage.py _manage.py
#If all ok, do the merge
diff --line-format %L manage.py custom/_manage.py >manage.py
```

### upgrading python, django

check pyupgrade args: [--py312-plus]
django-upgrade args: [--target-version, "5.0.4"]
