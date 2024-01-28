from django.db import models

# Create your models here.
class Task(models.Model):
    PRIORTIY_CHOICES = [
        (1, 'Low'),
        (2, 'Meduim'),
        (3, 'High')
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    priority = models.IntegerField(choices=PRIORTIY_CHOICES)
    due_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
