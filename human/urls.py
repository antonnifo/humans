from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
        path('', include('django.contrib.auth.urls')),
        path('dashboard/', views.dashboard, name="dashboard"),
        path('register/', views.register, name='register'),
        path('edit/', views.edit, name='edit'),
]


