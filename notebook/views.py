from django.shortcuts import render, get_object_or_404
from .models import Notebook, Note
import markdown
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from mdx_math import MathExtension
import re


def index(request):
    notebook_list = Notebook.objects.all()
    return render(request, 'notebook/index.html', context={
        'notebook_list': notebook_list,
    })


def details(request, pk):
    notebook = get_object_or_404(Notebook, pk=pk)
    contents = notebook.note_set.all()
    return render(request, 'notebook/details.html', context={
        'notebook': notebook,
        'contents': contents,
    })


def materials(request, pk):
    material = get_object_or_404(Note, pk=pk)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        MathExtension(enable_dollar_delimiter=True),
        # 'mdx_math',
        TocExtension(slugify=slugify),
    ])
    material.body = md.convert(material.body)
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    material.toc = m.group(1) if m is not None else ''
    return render(request, 'notebook/materials.html', context={
        'material': material,
    })
