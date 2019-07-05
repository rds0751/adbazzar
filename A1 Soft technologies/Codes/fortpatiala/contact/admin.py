# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
# Register your models here.
admin.site.register(Contact, ContactAdmin)