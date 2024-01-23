from django.urls import path
from . import views

urlpatterns = [
    path('', views.WebScraper.as_view(), name="web-scraper-view"),
]
