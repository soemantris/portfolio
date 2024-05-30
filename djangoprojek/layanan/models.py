from django.db import models

# Create your models here.
class GroupService(models.Model):
    title       = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Testimony(models.Model):
    full_name   = models.CharField(max_length=70)
    work        = models.CharField(max_length=80)
    review      = models.TextField(max_length=100)
    photos      = models.ImageField(upload_to='layanan/', default='layanan/testimony.png')
    pub_date    = models.DateTimeField(auto_now_add=True)
    update      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
