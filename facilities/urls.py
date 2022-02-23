from django.contrib import admin
from django.urls import path, include
from facilities import views as facility_views
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('register/', facility_views.register, name='register'),
    path('login/',
         auth_views.LoginView.as_view(template_name='facilities/login.html'),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='facilities/logout.html'),
         name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
