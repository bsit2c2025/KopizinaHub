# KopizinaHub Django application

This directory contains the Django application. The canonical product and technical specifications are maintained in the repository's [`docs/`](../docs/README.md) directory. Start with the [repository README](../README.md) and [contributor guide](../CONTRIBUTING.md) for project-wide guidance.

## Requirements

- Python 3.11 or newer
- SQLite (default) or MySQL
- MySQL deployments: `mysqlclient` (optional dependency, install separately)

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit:

- Public site: `http://127.0.0.1:8000/`
- Staff login: `http://127.0.0.1:8000/login/`
- Staff dashboard: `http://127.0.0.1:8000/dashboard/`
- Django admin: `http://127.0.0.1:8000/admin/`

The dashboard requires an authenticated staff user or superuser. Create local accounts with Django's management command; the project does not ship demo credentials.

## Configuration

Settings can be supplied through environment variables or a local `.env` file in this directory. `.env` is optional; SQLite and local development defaults are used when values are omitted.

```dotenv
DJANGO_SECRET_KEY=replace-with-a-long-random-secret
DJANGO_DEBUG=1
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
DJANGO_CSRF_TRUSTED_ORIGINS=
DJANGO_TIME_ZONE=Asia/Manila
```

To use MySQL, install its driver and set `DB_ENGINE=mysql`, `MYSQL_DATABASE`, `MYSQL_USER`, `MYSQL_PASSWORD`, `MYSQL_HOST`, and `MYSQL_PORT`. Run migrations after configuring the database.

Before deployment, set a private secret key, use `DJANGO_DEBUG=0`, configure allowed hosts and trusted HTTPS origins, run `python manage.py collectstatic --noinput`, and serve the WSGI application over HTTPS. See [`docs/specs/architecture.md`](../docs/specs/architecture.md) for the configuration contract.
