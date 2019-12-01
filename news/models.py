from django.db import models

# Create your models here.

class NewsPost(models.Model):
    topic = models.CharField(max_length=50);
    body = models.TextField();
    author = models.CharField(max_length=50);

    created = models.DateField(auto_now_add=True);

    published = models.BooleanField();
