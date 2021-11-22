from django.db import models

# Create your models here.
class Poem(models.Model):

    name = models.CharField(max_length=44)
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

