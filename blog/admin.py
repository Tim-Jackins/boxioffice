from django.contrib import admin 
from .models import Post 

def post_publish(modeladmin, request, queryset):
    for post in queryset:
        post.publish()
post_publish.short_description = 'Publish post'

class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post
    
    actions = [post_publish, ]

admin.site.register(Post, PostAdmin)
