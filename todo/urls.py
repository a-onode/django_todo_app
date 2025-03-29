from django.urls import path

from .views import IndexView, CreateView

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('create/', CreateView.as_view(), name='create'),
]
