# Behavior specification

## Route behavior

| Method | Path | Access | Expected behavior |
| --- | --- | --- | --- |
| GET | `/` | Public | Render the public landing page. |
| POST | `/api/public/reservations/` | Public, CSRF-protected | Validate a reservation; return JSON success with the created ID or a JSON validation error with HTTP 400. Other methods are rejected. |
| GET | `/login/` | Public | Render the staff login form. |
| POST | `/login/` | Public | Authenticate through Django's session login. Successful login redirects to `/dashboard/`. |
| POST | `/logout/` | Authenticated session | End the session and redirect to `/`. |
| GET | `/dashboard/` | Staff or superuser | Show total, pending, confirmed, and upcoming counts plus recent reservations. |
| GET | `/dashboard/reservations/` | Staff or superuser | Show reservations; support optional `q`, `status`, and `date` query filters. Search checks name, contact, and notes. |
| GET, POST | `/dashboard/reservations/add/` | Staff or superuser | Show and process a staff reservation form, including status. A valid submission creates a reservation and redirects to the list. |
| GET, POST | `/dashboard/reservations/<id>/edit/` | Staff or superuser | Show and process an edit form. A valid submission updates the reservation and redirects to the list. |
| POST | `/dashboard/reservations/<id>/delete/` | Staff or superuser | Delete the reservation and redirect to the list. Deletion must not be performed through GET. |
| GET | `/dashboard/reports/` | Staff or superuser | Show counts grouped by status, seating preference, and requested date for an inclusive date range. Default range is today and the preceding 29 days. |
| GET | `/admin/` | Django admin user | Serve the built-in Django admin site. |

Unauthenticated access to staff dashboard views redirects to `/login/`. Authenticated users who are neither staff nor superusers are redirected to `/` with an access message.

## Reservation validation

- Required form fields are name, contact, preferred date, arrival time, and party size.
- Seating preference uses one of the configured choices; it defaults to “Any available seat.”
- Notes are optional.
- A preferred date earlier than the server's local date is invalid.
- Public submissions always start with `pending` status. Only staff forms may set status directly.
- Invalid public submissions return status 400 and JSON containing a general error and field errors.

## Reports and filters

- The report range is inclusive.
- `from` and `to` accept ISO dates (`YYYY-MM-DD`). Missing endpoints use the default range.
- If a report date cannot be parsed, show a validation message and retain the usable default/parsed range.
- If the start date is after the end date, show a validation message and swap the endpoints.
- Empty filter values do not restrict the reservation list.

## Acceptance criteria for changes

Changes to these behaviors must preserve the stated access rules and HTTP methods. Add acceptance criteria for any new route or altered response, including valid input, invalid input, unauthorized access, and the expected redirect/status code.
