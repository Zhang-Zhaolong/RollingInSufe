from django.contrib import admin
from .models import Note, Notebook, Course
# Register your models here.


class NotebookAdmin(admin.ModelAdmin):
    list_display = ['notebook_name', 'created_time', 'course', 'author']
    fields = ['notebook_name', 'course', 'tags', 'abstract', 'foreword']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'in_notebook']
    fields = ['title', 'body', 'in_notebook']



admin.site.register(Note, NoteAdmin)
admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Course)
