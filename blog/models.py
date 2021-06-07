from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='documents/', null=True)
    title = models.CharField(max_length=50, null=True)
    caption = models.TextField(null=True)
    date_created = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super(Blog, self).save(*args, **kwargs)
        return self.id
        super().save()

    def __str__(self):
        return "{}".format(self.title)