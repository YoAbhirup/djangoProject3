from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name="Index"),
    path("Abhirup", views.Abhirup, name="Abhirup"),
    path("<str:name>",views.greet,name="Greet")
]