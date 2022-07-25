from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('register/', views.RegisterFormView.as_view()),
    path('login/', views.LoginFormView.as_view()),
    path('logout/', views.LogoutView.as_view())
]