from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Главная страница')

def group(request):
    return HttpResponse(f'Посты групп')

def group_posts(request, slug):
    return HttpResponse(f'Посты группы {slug}')