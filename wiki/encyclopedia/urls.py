from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("page/"'<title>'"/", views.search, name='page'),
    path("page/"'<title>'"/edit", views.editpage, name = "edit"),
    path("create", views.create, name="create")
]
