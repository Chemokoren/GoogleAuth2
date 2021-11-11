from django.urls import path
from .views import view_name

urlpatterns = [
    path('', view_name, name="view_name"),
]   