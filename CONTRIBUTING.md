# Contributing to KopizinaHub

Thank you for helping improve KopizinaHub. This guide applies to changes in the Django application and its documentation.

## Before changing code

1. Read [`docs/README.md`](docs/README.md) and the specs relevant to your change.
2. Check whether the requested behavior is already specified or listed as a future idea.
3. For a behavior or architecture change, update the relevant spec first. Include the user need, expected behavior, edge cases, and acceptance criteria. Keep proposals clearly marked until they are accepted.
4. Implement only behavior covered by the current spec. If implementation reveals a missing requirement, update the spec and explain the decision in the change.

## Development setup

From the repository root:

```bash
cd kopizina-django-export
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Use a local `.env` only when configuration overrides are needed. Never commit `.env`, credentials, local databases, virtual environments, or generated archives.

## Implementation guidelines

- Keep Django application code under `kopizina-django-export/` and project-level specifications under `docs/specs/`.
- Follow the existing Django patterns: models and migrations for persisted data, forms for input validation, views for request handling, and templates for rendered pages.
- Require staff access for internal reservation operations. Keep public reservation submission limited to the fields and validation defined in the specs.
- Add a migration whenever a model change requires one; commit the migration with the code.
- Keep secrets and environment-specific configuration out of source control.
- Update specs and user-facing documentation when routes, setup, configuration, or behavior changes.

## Verification

Run the relevant checks before submitting a change:

```bash
cd kopizina-django-export
python manage.py check
python manage.py test
```

For model changes, also verify migrations with `python manage.py makemigrations --check`. Include any manual browser checks that matter, such as public form validation or staff-only access.

## Submitting a change

Keep changes focused. In your pull request or review description, summarize the user-visible behavior, link the updated spec, list migrations or configuration changes, and report the checks you ran and their results. Call out any requirement that remains unresolved instead of silently inventing behavior.
