from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=255)
    memo = models.TextField(null=True, blank=True)
    due_at = models.DateField()
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
