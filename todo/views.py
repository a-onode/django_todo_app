from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import Todo


# Create your views here.
class IndexView(ListView):
    template_name = 'index.html'
    model = Todo


class CreateView(CreateView):
    template_name = 'create.html'
    model = Todo
    fields = ('title', 'memo', 'due_at')
    success_url = reverse_lazy('index')
