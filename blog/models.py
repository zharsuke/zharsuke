from django.db import models
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField

# Create your models here.

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    image = CloudinaryField('image', null=True)
    title = models.CharField(max_length=100, null=True)
    caption = models.TextField(null=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created',]

    def save(self, *args, **kwargs):
        super(Blog, self).save(*args, **kwargs)
        return self.id
        super().save()

    def __str__(self):
        return "{}".format(self.title)