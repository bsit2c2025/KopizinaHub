from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("api/public/reservations/", views.public_reservation_api, name="public_reservation_api"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/reservations/", views.reservation_list, name="reservation_list"),
    path("dashboard/reservations/add/", views.reservation_create, name="reservation_create"),
    path("dashboard/reservations/<int:pk>/edit/", views.reservation_update, name="reservation_update"),
    path("dashboard/reservations/<int:pk>/delete/", views.reservation_delete, name="reservation_delete"),
    path("dashboard/reports/", views.reports, name="reports"),
]
