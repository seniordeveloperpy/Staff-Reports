from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),


    # Avtorizatsiya
    path('log-in/', views.log_in, name='log_in'),
    path('log-out/', views.log_out, name='log_out'),


    # Staff 
    path('create-staff', views.create_staff, name='create_staff'),
    path('list-staff', views.list_staff, name='list_staff'),
    path('update-staff/<int:id>/', views.update_staff, name='update_staff'),
    path('delete-staff/<int:id>/', views.delete_staff, name='delete_staff'),


    # Attendance reports
    path('list-attendance', views.list_attendance, name='list_attendance'),


    # Edit profile staff
    path('edit-profile/<int:id>/', views.edit_profile, name='edit_profile'),
    
]