from django.urls import path
from . import views

app_name = "To-Do-List App"
urlpatterns = [
    path("", views.index, name = "Index"),
    path("new/", views.create, name = "Create"),
    path("check/", views.check, name = "Check")
]