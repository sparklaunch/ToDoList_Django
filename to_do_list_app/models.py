from django.db import models

# Create your models here.
class Item(models.Model):
    content = models.CharField(max_length = 255)
    is_done = models.BooleanField(default = False)