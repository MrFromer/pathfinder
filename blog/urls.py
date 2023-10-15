from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name = "index"),
    path("abc/", views.saveforms, name="saveforms"),
    path("page_choice/", views.page_choice, name="page_choice"),
    path("list/", views.list, name="list_character"),
    path('edit/<int:id>/', views.edit, name = "edit"),
    #path('edit_1_2/<int:id>/', views.edit_1_2, name = "edit_1_2"),
    #path('edit_1_2/', views.edit_1_2, name = "edit_1_2_no_id"),
    #path('edit_1_3/<int:id>/', views.edit_1_3, name = "edit_1_3"),
    #path('edit_1_2/', views.edit_1_2, name = "edit_1_3_no_id"),
    path('about_site', views.about_site, name = "about_site"),
    #path('<int:id>/delete', views.delete, name = "delete")
]