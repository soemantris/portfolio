from django.contrib import admin
from .models import Article, Category

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','categories','pub_date','images')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','description','pub_date')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)