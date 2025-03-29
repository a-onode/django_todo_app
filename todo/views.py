from django.views.generic import ListView

from .models import Todo


# Create your views here.
class IndexView(ListView):
    template_name = 'index.html'
    model = Todo
