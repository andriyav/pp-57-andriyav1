from django.contrib import admin
from .models import Author


#
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'id')
    fields = [('name', 'surname', 'patronymic'), 'books']
    list_filter = ('surname', 'books', 'id')


admin.site.register(Author, AuthorAdmin)