from django.db import models

# Create your models here.
class home(models.Model):

    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='pictures')
    description = models.TextField()

    def __str__(self):
        return self.name
class mypage(models.Model):

    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name
