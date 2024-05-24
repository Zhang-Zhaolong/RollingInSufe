from django.contrib import admin
from .models import Category, Article, Tag
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'author']
    fields = ['title', 'abstract', 'body', 'category', 'tags']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)

