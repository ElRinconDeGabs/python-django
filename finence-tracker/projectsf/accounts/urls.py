from django.urls import path
from . import views

urlpatterns = [
    path('sing-up/', views.signup_view, name='sing_up'),
]