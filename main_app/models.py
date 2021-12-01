from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Poem(models.Model):

    name = models.CharField(max_length=44)
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']



# blank is for django? null is for db? 
# blank=True, null=True,

# to being db user id at 1 or no? 
# default=1 