from django.contrib import admin
from tickets.models import CustomUser, Ticket
from django.contrib.auth.admin import UserAdmin

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Ticket)