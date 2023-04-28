from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'count')
    list_filter = ('id', 'name', 'authors')
    fieldsets = [
        (
            None,
            {
                "fields": ['name', 'description'],
            },
        ),
        (
            "Кількість книги",
            {

                "fields": ['count'],
            },
        ),
    ]


admin.site.register(Book, BookAdmin)