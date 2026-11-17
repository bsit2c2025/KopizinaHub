from datetime import date, timedelta
from functools import wraps

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from .forms import AdminReservationForm, ReservationForm
from .models import Reservation


def home(request):
    return render(request, "reservations/home.html")


@require_POST
def public_reservation_api(request):
    form = ReservationForm(request.POST)
    if not form.is_valid():
        return JsonResponse({"error": "Please check the highlighted fields.", "fields": form.errors.get_json_data()}, status=400)
    reservation = form.save()
    return JsonResponse({"ok": True, "id": reservation.pk})


def staff_required(view):
    @login_required(login_url="/login/")
    @wraps(view)
    def wrapped(request, *args, **kwargs):
        if not request.user.is_staff and not request.user.is_superuser:
            messages.error(request, "This dashboard is restricted to staff users.")
            return redirect("/")
        return view(request, *args, **kwargs)

    return wrapped


@staff_required
def dashboard(request):
    today = timezone.localdate()
    context = {
        "total_records": Reservation.objects.count(),
        "pending_count": Reservation.objects.filter(status="pending").count(),
        "confirmed_count": Reservation.objects.filter(status="confirmed").count(),
        "upcoming_count": Reservation.objects.filter(preferred_date__gte=today).exclude(status="cancelled").count(),
        "recent_reservations": Reservation.objects.all()[:8],
    }
    return render(request, "reservations/dashboard.html", context)


@staff_required
def reservation_list(request):
    reservations = Reservation.objects.all()
    query = request.GET.get("q", "").strip()
    status = request.GET.get("status", "").strip()
    date_filter = request.GET.get("date", "").strip()
    if query:
        reservations = reservations.filter(Q(name__icontains=query) | Q(contact__icontains=query) | Q(notes__icontains=query))
    if status:
        reservations = reservations.filter(status=status)
    if date_filter:
        reservations = reservations.filter(preferred_date=date_filter)
    return render(request, "reservations/reservation_list.html", {
        "reservations": reservations,
        "query": query,
        "status": status,
        "date_filter": date_filter,
        "status_choices": Reservation.STATUS_CHOICES,
    })


@staff_required
def reservation_create(request):
    form = AdminReservationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Reservation created.")
        return redirect("reservation_list")
    return render(request, "reservations/reservation_form.html", {"form": form, "heading": "Create reservation", "submit_label": "Create record"})


@staff_required
def reservation_update(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    form = AdminReservationForm(request.POST or None, instance=reservation)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Reservation updated.")
        return redirect("reservation_list")
    return render(request, "reservations/reservation_form.html", {"form": form, "heading": "Update reservation", "submit_label": "Save changes", "reservation": reservation})


@staff_required
@require_POST
def reservation_delete(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    reservation.delete()
    messages.success(request, "Reservation deleted.")
    return redirect("reservation_list")


@staff_required
def reports(request):
    today = timezone.localdate()
    start = today - timedelta(days=29)
    end = today
    from_value = request.GET.get("from", "")
    to_value = request.GET.get("to", "")
    try:
        if from_value:
            start = date.fromisoformat(from_value)
        if to_value:
            end = date.fromisoformat(to_value)
    except ValueError:
        messages.error(request, "Use valid dates in YYYY-MM-DD format.")
    if start > end:
        messages.error(request, "The report start date must be before the end date.")
        start, end = end, start
    window = Reservation.objects.filter(preferred_date__range=(start, end))
    status_breakdown = window.values("status").annotate(total=Count("id")).order_by("status")
    seating_breakdown = window.values("seating_preference").annotate(total=Count("id")).order_by("-total")
    daily_breakdown = window.values("preferred_date").annotate(total=Count("id")).order_by("preferred_date")
    return render(request, "reservations/reports.html", {
        "from_value": start.isoformat(),
        "to_value": end.isoformat(),
        "total_records": window.count(),
        "status_breakdown": status_breakdown,
        "seating_breakdown": seating_breakdown,
        "daily_breakdown": daily_breakdown,
    })
