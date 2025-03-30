from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy

from .models import Todo


# Create your views here.
class IndexTodo(ListView):
    template_name = 'index.html'
    model = Todo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['incomplete_count'] = Todo.objects.filter(is_done=False).count()
        context['complete_count'] = Todo.objects.filter(is_done=True).count()
        context['incomplete_todos'] = Todo.objects.filter(is_done=False)
        context['complete_todos'] = Todo.objects.filter(is_done=True)
        return context


class CreateTodo(CreateView):
    template_name = 'create.html'
    model = Todo
    fields = ('title', 'memo', 'due_at')
    success_url = reverse_lazy('index')


class DeleteTodo(DeleteView):
    template_name = 'delete.html'
    model = Todo
    success_url = reverse_lazy('index')


def change_status(request, pk):
    todo = Todo.objects.get(pk=pk)
    if todo.is_done:
        todo.is_done = False
    else:
        todo.is_done = True
    todo.save()
    return redirect('index')
