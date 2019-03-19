#pylint: disable-msg=no-member
from django.shortcuts import render
from django.utils import timezone

from .models import Post
from .forms import NewPostForm
from django.contrib.auth.decorators import login_required
from markdownx.fields import MarkdownxFormField
from django.urls import reverse

def post_list(request):
    print(Post.objects.all().order_by('published_date'))
    posts = Post.objects.all().order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def make_post(request):
    if request.POST:
        newPost = Post(
            author=request.POST.get('author'),
            title=request.POST.get('title'),
            text=request.POST.get('text'),
        )

        newPost.save()

        return render(request, 'blog/post_list.html')
    else:
        form = NewPostForm
        context = {'form' : form}
        return render(request, 'blog/new_post.html', context)
