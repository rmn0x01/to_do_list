from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()
class Task(models.Model):
    author = models.ForeignKey(User,related_name='tasks',on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    description = models.TextField()
    deadline = models.DateField()
    CATEGORIES = (
        ('1','To-do'),
        ('2','On-going'),
        ('3','Done')
    )
    status = models.CharField(max_length=1,choices=CATEGORIES)

    class Meta:
        ordering = ['deadline']

    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)
    
    def get_absolute_url(self):
        return reverse("to_do_list:task_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title