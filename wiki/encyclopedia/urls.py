from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("page/"'<file>', views.title),
    path("randompage", views.rand, name="rand")
]
