from django.urls import path
from . import views

app_name = "library"

urlpatterns = [
    path("", views.book_list, name="book_list"),
    path("<int:pk>/", views.book_detail, name="book_detail"),
    path("create/", views.book_create, name="book_create"),
]
