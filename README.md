# KopizinaHub

KopizinaHub is a Django application for the Kopizina café website and staff reservation workflow. The public site accepts reservation requests; authorized staff can review and manage them through a dashboard.

## Documentation

Project requirements and implementation guidance are maintained as small, linked Markdown specs in [`docs/README.md`](docs/README.md). Start there before making product or architecture changes. The contributor workflow is in [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Run locally

The Django project is in `kopizina-django-export/`. From the repository root:

```bash
cd kopizina-django-export
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/`. Staff sign in at `/login/`, use the dashboard at `/dashboard/`, and access Django admin at `/admin/`.

SQLite is the default local database. The application reads optional configuration from a `.env` file in `kopizina-django-export/`; see [the application README](kopizina-django-export/README.md) for database and deployment settings. Do not commit credentials or local database files.

## Current scope

The current application includes the public landing page, reservation intake, staff login, reservation management, dashboard summaries, and date-range reports. Loyalty cards, transaction history, and prevention of conflicting/double bookings are ideas recorded for future specification; they are not represented as implemented features.

## Project Screenshots

Landing Page
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/264aca63-c742-4259-b64b-d8e9e2f0a618" />
