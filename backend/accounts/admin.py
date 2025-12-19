from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    # Added 'username' to this list so you can see the auto-generated result
    list_display = ('email', 'username', 'role', 'is_staff') 
    ordering = ('email',)