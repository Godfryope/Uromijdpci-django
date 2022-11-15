from django.contrib import admin
from .models import Blog, Comment



# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)} 

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'blog', 'created_on', 'aprroved')
    list_filter = ('aprroved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(aprroved=True)

# admin.site.register(Blog, BlogAdmin)