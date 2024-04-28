from django.urls import path
from . import views

urlpatterns = [
    path('locations/', views.locations),
    path('<int:location_pk>/stations/', views.stations),
    path('stations/', views.station_list),
    path('stations/<int:station_pk>/', views.station_all),
]