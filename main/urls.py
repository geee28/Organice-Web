from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("viewalllists/", views.viewalllists, name="viewalllists"),
    path("list<int:id>/", views.viewlist, name="viewlist"),
    path("createlist/", views.createlist, name="createlist"),
    path("createnote/", views.createnote, name="createnote"),
    path("viewallnotes/", views.viewallnotes, name="viewallnotes"),
    path("note<int:nid>/", views.viewnote, name="viewnote"),

]
