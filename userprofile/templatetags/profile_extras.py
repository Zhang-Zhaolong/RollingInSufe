from django import template
from django.shortcuts import get_object_or_404
from ..models import Profile

register = template.Library()


@register.inclusion_tag('userprofile/inclusions/_show_photo.html', takes_context=True)
def show_photo(context, user_pk):
    profile = get_object_or_404(Profile, user_id=user_pk)
    return {
        'profile': profile,
    }


