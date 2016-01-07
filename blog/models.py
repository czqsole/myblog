from django.db import models

class Blog(models.Model):
    #id =
    pub_time = models.DateField('date published')
    title = models.CharField(max_length=100)
    summary = models.TextField()
    article = models.TextField()
