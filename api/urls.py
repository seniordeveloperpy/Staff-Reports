from . import views
from django.urls import path


urlpatterns = [
    path('staff-list', views.staff_list),
    path('attendance-create', views.attendance_create),
    
]
