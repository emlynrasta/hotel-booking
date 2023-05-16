from django.urls import path
from . import views

#URL configs
urlpatterns = [
    path('', views.user_login, name='login'),
]
