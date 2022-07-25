from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name = "index"),
    path("abc/", views.saveforms, name="saveforms"),
    path("page_choice/", views.page_choice, name="page_choice"),
    path('list/', views.list, name="list_character"),
    path('edit/<int:id>/', views.edit, name = "edit"),
    path('about_site', views.about_site, name = "about_site"),
]