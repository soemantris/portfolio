from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Category(models.Model):
    title           = models.CharField(max_length=30)
    description     = models.CharField(max_length=100, blank=True, null=True)
    slug_category   = models.SlugField(blank=True, null=True, editable=False)
    pub_date        = models.DateTimeField(auto_now_add=True)
    update          = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug_category = slugify(self.title)
        return super(Category, self).save(*args, **kwargs)

class Project(models.Model):
    categories      = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    title           = models.CharField(max_length=50)
    description     = RichTextUploadingField(blank=True, null=True)
    visit_site      = models.URLField(blank=True,null=True)
    images          = models.ImageField(upload_to='projek/', default='projek/projek.png')
    slug            = models.SlugField(blank=True, editable=False)
    pub_date        = models.DateTimeField(auto_now_add=True)
    update          = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Project, self).save(*args, **kwargs)