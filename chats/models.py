from django.db import models

from django.contrib.auth.models import User,Group

from django.utils.text import slugify

# Create your models here.


class Room(models.Model):
    room_name = models.CharField(max_length=300)
    slug = models.SlugField(null=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.room_name)
        super(Room,self).save(*args, **kwargs)

    def __str__(self):
        return self.room_name

class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.user} : {self.content}'


