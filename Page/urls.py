from django.urls import path

from Page import views

urlpatterns = [
    path("", views.index, name="page_index"),
]