# Product specification

## Status

This document describes the current product scope for the Django application. The listed workflows are reflected in the current code unless explicitly marked as a future idea.

## Purpose

KopizinaHub provides a public web presence for Kopizina and a staff workflow for receiving and managing table reservation requests.

## Users

- **Visitor:** views the public landing page and submits a reservation request.
- **Staff member:** signs in and reviews, creates, edits, or deletes reservations, and views reservation summaries and reports.
- **Administrator:** uses Django admin to manage application data and Django accounts.

## Current workflows

1. A visitor opens the public landing page and submits the reservation form.
2. The server validates the submitted fields. Invalid requests receive a JSON error response; valid requests create a reservation with `pending` status and receive the new reservation ID.
3. A staff member signs in and can view the dashboard, search/filter reservations, manage reservation records, and view date-range summaries.
4. A staff member can sign out. Non-staff authenticated users must not access staff dashboard views.

See [`behavior.md`](behavior.md) for route-level requirements and [`data.md`](data.md) for stored reservation fields.

## Product constraints

- Reservation requests are stored in the configured Django database.
- A reservation expresses a requested date/time and party size; the current application does not promise or guarantee seating availability.
- Staff access uses Django's built-in user and session authentication. Staff authorization is based on `is_staff` or `is_superuser`.
- The public reservation endpoint accepts POST requests and is protected by Django's configured CSRF middleware for browser form submissions.

## Future ideas (not implemented requirements)

The following appeared in earlier project notes. They need separate decisions and acceptance criteria before implementation:

- Loyalty/customer card
- Transaction history
- Preventing conflicting reservations and double booking

For double-booking prevention, a future spec must define what counts as a conflict (including capacity, party size, table/seat availability, time windows, and cancellation behavior) and how concurrent submissions are handled. Do not infer those rules from the current reservation form.
