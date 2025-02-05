from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'body_preview', 'thumb', 'date']  # Title, date and a preview of the body
    search_fields = ['title', 'body']

    def body_preview(self, obj):
        preview = obj.body[:50]  # Get first 50 characters
        if len(obj.body) > 50:  # If the body is longer than 50 characters
            preview += "..."  # Add "..." to indicate more content
        return preview # Display first 50 characters of the body as a preview
    body_preview.short_description = 'Body Preview'  # Customize the column title
