from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("page/"'<file>', views.title),
    path("page/"'<title>'"/", views.search),
    path("page/"'<title>'"/edit", views.editpage),
    path("saving_changes",views.save)
]
