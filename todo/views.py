from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy

from .models import Todo


# Create your views here.
class IndexTodo(ListView):
    template_name = 'index.html'
    model = Todo


class CreateTodo(CreateView):
    template_name = 'create.html'
    model = Todo
    fields = ('title', 'memo', 'due_at')
    success_url = reverse_lazy('index')


class DeleteTodo(DeleteView):
    template_name = 'delete.html'
    model = Todo
    success_url = reverse_lazy('index')
