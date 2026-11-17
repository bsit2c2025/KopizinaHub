# Architecture specification

## Runtime and framework

- The application is a server-rendered Django project using Django templates and plain JavaScript/CSS.
- Dependencies are declared in `kopizina-django-export/requirements.txt`.
- SQLite is the default database. MySQL can be selected through environment configuration and requires the optional `mysqlclient` driver.
- Django's built-in authentication, sessions, admin, ORM, forms, and CSRF protection are used.

## Source layout

All paths below are relative to `kopizina-django-export/`:

- `kopizina_project/`: Django settings, root URL configuration, and WSGI entry point.
- `reservations/`: reservation model, forms, views, app URLs, admin registration, and migrations.
- `templates/`: public pages, staff dashboard pages, and login template.
- `static/`: CSS, JavaScript, and image assets.
- `manage.py`: local Django command entry point.

The root-level `docs/specs/` directory contains product and technical requirements and is the canonical documentation source.

## Request and persistence boundaries

- URL configuration maps requests to views in `reservations.views` or Django's built-in auth/admin views.
- Forms own reservation input validation; views coordinate requests, permissions, persistence, and responses.
- `Reservation` is the canonical persisted reservation entity. Database schema changes are made through Django migrations.
- Templates render HTML. The public reservation intake responds with JSON.
- Staff-only access is enforced in view code. New internal views must use equivalent staff authorization.

## Configuration

Settings are read from environment variables, optionally loaded from `.env` in the Django project directory:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG`
- `DJANGO_ALLOWED_HOSTS` (comma-separated hostnames)
- `DJANGO_CSRF_TRUSTED_ORIGINS` (comma-separated origins)
- `DJANGO_TIME_ZONE`
- `DB_ENGINE` (`sqlite` by default; use `mysql` for MySQL)
- `MYSQL_DATABASE`, `MYSQL_USER`, `MYSQL_PASSWORD`, `MYSQL_HOST`, `MYSQL_PORT`

Production deployments must set a private secret key, disable debug mode, configure allowed hosts and trusted HTTPS origins, and serve static assets appropriately. Secrets must not be committed.

## Architectural change criteria

Introducing a new service, package, API format, authentication provider, or storage system requires an explicit spec update describing its need, boundaries, configuration, and operational implications. Prefer existing Django facilities when they satisfy the requirements.
