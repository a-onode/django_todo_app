from django.urls import path

from .views import IndexTodo, CreateTodo, DeleteTodo

urlpatterns = [
    path('index/', IndexTodo.as_view(), name='index'),
    path('create/', CreateTodo.as_view(), name='create'),
    path('delete/<int:pk>/', DeleteTodo.as_view(), name='delete'),
]
