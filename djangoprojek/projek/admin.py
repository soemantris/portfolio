from django.contrib import admin
from .models import Project, Category

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','categories','visit_site','pub_date')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','description','pub_date')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)