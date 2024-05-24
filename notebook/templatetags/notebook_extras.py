from django import template
from ..models import Notebook, Note
from django.shortcuts import get_object_or_404

register = template.Library()


@register.inclusion_tag('notebook/inclusions/_show_contents.html', takes_context=True)
def show_contents(context, notebook_pk):
    notebook = get_object_or_404(Notebook, pk=notebook_pk)
    contents = notebook.note_set.all()
    return {
        'contents': contents,
        'notebook': notebook,
    }