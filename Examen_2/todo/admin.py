from django.contrib import admin
from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'completed', 'created_at']
    list_filter = ['completed', 'created_at', 'user']
    search_fields = ['title', 'user__username']
    list_editable = ['completed']
    ordering = ['-created_at']
