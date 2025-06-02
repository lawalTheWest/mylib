from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<uuid:pk>/', views.book_detail, name='book_detail'),
]
