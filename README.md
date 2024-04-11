# Setup environment
```bash
  python -m venv .venv
  source .venv.bin/activate
  python -m pip install pip-tools
  deactivate
  pip-compile
  pip-sync --ask
  source .venv/bin/activate
```
# Setup project
```bash
django-admin startproject main .
```

## Setup manage.py
```bash
diff manage.py _manage.py
#If all ok, do the merge
diff --line-format %L manage.py _manage.py >manage.py
```

## upgrading python, django
  check pyupgrade args: [--py312-plus]
  django-upgrade  args: [--target-version, "5.0.4"]
