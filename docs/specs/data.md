# Data specification

## Reservation

The reservation record is implemented by `reservations.Reservation`.

| Field | Type | Required | Rules / meaning |
| --- | --- | --- | --- |
| `name` | String, max 120 | Yes | Name supplied by the customer. |
| `contact` | String, max 160 | Yes | Customer contact detail. The current spec does not constrain it to a particular contact format. |
| `preferred_date` | Date | Yes | Requested reservation date; public forms reject dates before the local current date. |
| `arrival_time` | Time | Yes | Requested arrival time. Availability is not guaranteed by storing this value. |
| `party_size` | Choice string, max 12 | Yes | One of `1`, `2`, `3`, `4`, `5`, or `5+`. |
| `seating_preference` | Choice string, max 32 | Yes | `Quiet desk`, `Shared table`, or `Any available seat`; defaults to `Any available seat`. |
| `notes` | Text | No | Optional customer-provided note. |
| `status` | Choice string, max 12 | Yes | `pending`, `confirmed`, or `cancelled`; defaults to `pending`. |
| `created_at` | Date/time | System-set | Creation timestamp. |
| `updated_at` | Date/time | System-set | Updated whenever the record is saved. |

Records are ordered newest first. The model indexes `(preferred_date, status)` and `contact`.

## Data handling requirements

- Do not log or expose contact details and notes unnecessarily.
- Do not add customer information to documentation, fixtures, screenshots, or examples.
- Model changes must include the corresponding Django migration.
- A future availability/double-booking feature must specify its data constraints and concurrency behavior before changing the reservation schema.
