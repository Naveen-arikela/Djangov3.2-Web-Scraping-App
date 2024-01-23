from django.contrib import admin
from django.urls import path, include

#Comment
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('scrapwebapp.urls')),
]

def feature1():
    pass