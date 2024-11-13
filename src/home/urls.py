from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("preview/<int:pk>/", views.preview, name="preview-detail"),
]
