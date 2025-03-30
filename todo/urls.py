from django.urls import path

from .views import IndexTodo, CreateTodo, DeleteTodo, change_status

urlpatterns = [
    path('index/', IndexTodo.as_view(), name='index'),
    path('create/', CreateTodo.as_view(), name='create'),
    path('delete/<int:pk>/', DeleteTodo.as_view(), name='delete'),
    path('status/<int:pk>/', change_status, name='status'),
]
