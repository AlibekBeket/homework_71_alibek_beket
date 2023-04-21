from django.contrib import admin

from instagram.models import Posts, Comments


# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "img", "description", "likes", "comments", "created_at")
    list_filter = ("id", "user", "description", "likes", "comments", "created_at")
    search_fields = ("id", "user", "description", "likes", "comments", "created_at")
    fields = ("user", "description", "img", "likes", "comments")
    readonly_fields = ("id", "created_at")


admin.site.register(Posts, PostsAdmin)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "description", "post", "created_at")
    list_filter = ("id", "user", "description", "post", "created_at")
    search_fields = ("id", "user", "description", "post", "created_at")
    fields = ("user", "description", "post")
    readonly_fields = ("id", "created_at")


admin.site.register(Comments, CommentsAdmin)