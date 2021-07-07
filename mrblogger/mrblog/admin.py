from django.contrib import admin
from .models import Post,  BlogComment

# Register your models here.
admin.site.register((Post,BlogComment))

class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)