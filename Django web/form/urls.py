from django.urls import path
from . import views


app_name = "form"
urlpatterns = [
    path("", views.index, name = "start"),
    path("add", views.add, name = "add")
]