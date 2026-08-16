
from django.contrib import admin
from django.urls import path,include
from .views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/",Home,name="home"),
    path('tution/',include('tution.urls')),
]
