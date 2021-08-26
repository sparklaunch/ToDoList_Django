from django.urls import path
from . import views

app_name = "to_do_list"
urlpatterns = [
    path("", views.index, name = "index"),
    path("new", views.create, name = "create"),
    path("check/<int:item_index>", views.check, name = "check")
]