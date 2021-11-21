
from django.urls import path
from . import views

urlpatterns = [
    path(r'books/', views.BooksView.as_view()),
]