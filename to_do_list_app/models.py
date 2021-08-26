from django.db import models
from django.utils import timezone

# Create your models here.
class Item(models.Model):
    content = models.CharField(max_length = 255)
    is_done = models.BooleanField(default = False)
    created = models.DateTimeField(default = timezone.now())
    def __str__(self):
        return self.content