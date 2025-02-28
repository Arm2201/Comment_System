#from tkinter import Image
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Post(models.Model):
    image = models.ImageField(
        default = "default_foo.png", upload_to = "post_picture")
    caption = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User,  on_delete = models.CASCADE)
    def _str_(self):
        return f'{self.author.username}\'s Post- {self.title}'
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.Image.open)
        if img.height > 400 or img.width > 400:
                output_size = (300, 300)
                img.thumbnail(output_size) 
                img.save(self.image.path)
class Comment:
    pass

    