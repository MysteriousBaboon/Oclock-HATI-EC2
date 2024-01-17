from django.contrib import admin
from app.models import Student
from django.utils.html import format_html


@admin.register(Student)
class PriceAdmin(admin.ModelAdmin):
    # Variable or functions to show as columns
    list_display = ("first_name", 'last_name', "score")

    # Search bar
    search_fields = ["first_name", "last_name"]


