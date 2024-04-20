from django.urls import path, include
from dashboard.views import log_in

app_name = 'main'

urlpatterns = [
    path('', log_in),
    path('api/', include('api.urls'))
]