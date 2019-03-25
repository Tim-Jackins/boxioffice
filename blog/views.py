#pylint: disable-msg=no-member
from django.shortcuts import render
from django.utils import timezone

from .models import Post
from .forms import NewPostForm
from django.contrib.auth.decorators import login_required
from markdownx.fields import MarkdownxFormField
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.contrib.auth import get_user_model
User = get_user_model()

def post_list(request):
    posts = Post.objects.all().exclude(published_date=None).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def make_post(request):
    if request.POST:
        newPost = Post(
            author=User.objects.get(pk=request.POST.get('author')),
            title=request.POST.get('title'),
            content=request.POST.get('text'),
        )

        if request.POST.get('publish_now'):
            newPost.publish()

        newPost.save()

        return HttpResponseRedirect(reverse('blog'))
    else:
        form = NewPostForm()
        context = {'form' : form}
        return render(request, 'blog/new_post.html', context)
