# Project documentation

This directory is the canonical, AI-readable specification for KopizinaHub. Keep each document focused, link related requirements, and update the specs before implementing changes that alter product behavior or architecture.

## Start here

1. [`specs/product.md`](specs/product.md) — product purpose, users, supported workflows, and out-of-scope ideas.
2. [`specs/behavior.md`](specs/behavior.md) — routes, permissions, validation, and observable application behavior.
3. [`specs/data.md`](specs/data.md) — reservation fields, allowed values, and persistence expectations.
4. [`specs/architecture.md`](specs/architecture.md) — application structure, framework conventions, configuration, and boundaries.

Then inspect the relevant implementation in `kopizina-django-export/`. The code and migrations describe what is currently implemented; these specs describe the intended behavior. If they disagree, do not guess: identify the conflict, update the spec to reflect the accepted requirement, and then change the implementation.

## Spec-driven change process

For every feature or behavior change:

1. State the user need and scope in the relevant spec.
2. Write testable acceptance criteria, including permissions, invalid input, and important edge cases.
3. Implement the smallest change that satisfies those criteria.
4. Update migrations and docs when applicable.
5. Verify the acceptance criteria and report the checks performed.

Security, privacy, and data integrity requirements apply to all changes. Never put credentials, private customer data, or real reservation records in specs, examples, or fixtures.

## Documentation rules for AI and contributors

- Treat `specs/` as the project requirements, not as a task backlog or a substitute for inspecting the code.
- Distinguish implemented behavior from proposed behavior. Ideas without acceptance criteria are not authorization to implement them.
- Prefer precise examples and observable outcomes over vague terms such as “user-friendly” or “secure.”
- Keep one authoritative statement for each requirement and link to it instead of copying it into multiple files.
- When changing a route, field, permission, or setup step, update every directly affected spec and the root README as needed.
- Do not introduce dependencies, external services, or new product capabilities unless the relevant spec calls for them.

## Repository entry points

- User and developer setup: [`../README.md`](../README.md) and [`../CONTRIBUTING.md`](../CONTRIBUTING.md)
- Django application: [`../kopizina-django-export/`](../kopizina-django-export/)
- Current feature specification: [`specs/product.md`](specs/product.md)
