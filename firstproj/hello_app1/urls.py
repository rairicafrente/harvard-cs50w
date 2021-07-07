from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("rai", views.rai, name="rai"),
    path("<str:name>", views.greet, name="greet")
]
