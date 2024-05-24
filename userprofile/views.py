from django.shortcuts import render, get_object_or_404
from .models import Profile
import pyecharts.options as opts
from pyecharts.charts import WordCloud
from django.http import HttpResponse
import pandas as pd
from collections import Counter
import re
import jieba


def profiles(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    article_list = profile.user.article_set.all()
    notebook_list = profile.user.notebook_set.all()
    return render(request, 'userprofile/profile.html', context={
        'user_profile': profile,
        'article_list': article_list,
        'notebook_list': notebook_list,
    })


def counter2list(_counter):
    wordslist,nums = [],[]
    for item in _counter:
        wordslist.append(item[0])
        nums.append(item[1])
    return wordslist,nums


def wordcloud(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    article_list = profile.user.article_set.all()
    content = []
    for article in article_list:
        content.append(article.body)
    stopwords = pd.read_csv('./chinesestopword.txt', sep='\n', encoding='utf-8', names=['stopwords'], header=None,
                            quoting=3)
    pattern = re.compile('\d+')

    wordsCounter = Counter()
    for line in content:
        segs = jieba.lcut(line)
        for seg in segs:
            if len(seg) > 1 and seg != '\r\n' and re.search(pattern, seg) == None:
                wordsCounter[seg] += 1

    wordslist, nums = counter2list(wordsCounter.most_common(1000))
    c = (
        WordCloud()
        .add("", zip(wordslist, nums), shape='roundRect')
        .set_global_opts(title_opts=opts.TitleOpts(title="Ta的关键词"))
    )
    return HttpResponse(c.render_embed())
