from django.contrib import admin
from .models import ContactModel, About


class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'subject', 'message')
    list_display_links = ('name', 'email')


class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


admin.site.register(About, AboutAdmin)
admin.site.register(ContactModel, ContactAdmin)

