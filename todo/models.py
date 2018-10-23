from django.db import models
from companies.models import Company


class Todo(models.Model):
    description = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                related_name='todo_lists')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('completed', '-date_created')
