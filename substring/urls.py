from django.urls import path
from .views import longest_substring_view

urlpatterns = [
    path("", longest_substring_view, name="longest_substring"),
]