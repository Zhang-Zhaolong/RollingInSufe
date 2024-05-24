from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Article, Tag


def index(request):
    article_list = Article.objects.all()
    return render(request, 'article/index.html', context={
        'article_list': article_list,
    })


def details(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article/details.html', context={
        'article': article,
    })


def tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    article_list = Article.objects.filter(tags=tag)
    return render(request, 'article/article_list.html', context={
        'tag_name': tag.name,
        'article_list': article_list,
    })