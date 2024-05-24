from django import template
from ..models import Article, Category, Tag

register = template.Library()


@register.inclusion_tag('article/inclusions/_recent_articles.html', takes_context=True)
def show_recent_articles(context, num=5):
    recent_articles = Article.objects.all().order_by('-created_time')[:num]
    return {
        'recent_articles': recent_articles,
    }


@register.inclusion_tag('article/inclusions/_show_tags.html', takes_context=True)
def show_tags(context):
    tags_list = Tag.objects.all()
    return {
        'tags_list': tags_list,
    }
