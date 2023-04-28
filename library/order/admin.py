from django.contrib import admin
from .models import Order


# admin.site.register(Order)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'created_at', 'plated_end_at', 'end_at')

    list_filter = ('user', 'end_at')

    fieldsets = [
        (
            None,
            {
                "fields": ["book", "user"],
            },
        ),
        (
            "Планові та дійсні дати повернення книги",
            {

                "fields": ["plated_end_at", "end_at"],
            },
        ),
    ]


admin.site.register(Order, OrderAdmin)