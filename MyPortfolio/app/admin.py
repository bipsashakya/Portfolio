from django.contrib import admin
from app.models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('name',)