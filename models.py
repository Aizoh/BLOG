from django.db import models
from datetime import datetime

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    time = models.DateTimeField(default=datetime.now, blank=True)
    # to determine the name of the object created in admin site
    def __str__(self):
        return self.title

    # in the admin site to det prural for our model
    class Meta:
        verbose_name_plural = "posts"
        
