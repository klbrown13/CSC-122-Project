from django.contrib import admin
from .models import Post, Comment
# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
    list_display = [
        "title",
        "author",
        "company",
        "location",
        "job_type", 
        "internship_status", 
        "body",
    ]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)