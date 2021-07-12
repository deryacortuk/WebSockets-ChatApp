from django.urls import path
from . import views

app_name= "personal"
urlpatterns = [
    
    path('dashboard/',views.dashboard,name="dashboard"),
    
]