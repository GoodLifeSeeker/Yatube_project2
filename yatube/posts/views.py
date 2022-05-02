from django.shortcuts import get_object_or_404, render

from .models import Group, Post

NUMBER_OF_POSTS = 10

def index(request):
    template = 'posts/index.html'
    title = 'Последние записи'
    posts = Post.objects.all()
    context = {
        'title':title,
        'posts':posts
    }
    return render(request, template, context)

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group_list.html'
    title = 'Записи сообщества '
    posts = group.posts.all()[:NUMBER_OF_POSTS]
    context = {
        'title':title,
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)