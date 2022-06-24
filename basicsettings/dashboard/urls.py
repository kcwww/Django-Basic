from django.urls import path
from dashboard import views

urlpatterns = [
    path('',views.dashboardlist),
    path('first',views.dashboardfirst),
]