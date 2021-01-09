from django.urls import path , include
from django.contrib import admin
from django.views.generic.base import TemplateView
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name = 'signup'),
]