from django.db import models
from django.urls import reverse
from django.db.models import Q

class TaskManager(models.Model):
    task = models.CharField(max_length=1000)
    t_Creator = models.CharField(max_length=250)
    t_Assigned = models.CharField(max_length=250)
    t_Done = models.BooleanField(default=False)

    def get_absoulte_url(self):
        return reverse('sdlrs:detail', kwargs={'pk': self.pk})