from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.conf import settings

# Create your models here.
class Category(models.Model):
    title       = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    images      = models.ImageField(upload_to='kategori/', default='kategori/kategori.png')
    slug_categ  = models.SlugField(blank=True, editable=False)
    pub_date    = models.DateTimeField(auto_now_add=True)
    update      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug_categ = slugify(self.title)
        return super(Category, self).save(*args, **kwargs)
    
class Article(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    categories  = models.ForeignKey(Category, on_delete=models.CASCADE)
    title       = models.CharField(max_length=200, null=True)
    content     = RichTextUploadingField(blank=True, null=True)
    images      = models.ImageField(upload_to='artikel/', default='artikel/artikel.png')
    slug        = models.SlugField(blank=True, editable=False)
    pub_date    = models.DateTimeField(auto_now_add=True, editable=True)
    update      = models.DateTimeField(auto_now=True, editable=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)
    