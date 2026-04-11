# Locale / Translations

Translation source files (`.po`) are tracked in git. Compiled binary files (`.mo`) are not.

After cloning or pulling changes that include `.po` updates, you must compile the messages before translations will work at runtime:

```bash
django-admin compilemessages
```

Or via `manage.py`:

```bash
python manage.py compilemessages
```

This must also be run as part of any deployment or build process.
