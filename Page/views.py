from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    site = {
        'url': 'http://127.0.0.1:8000/',
        'title': '易部落阁',
    }
    page = {
        'title': site['title'] + ' 首页',
    }
    articles = [
        {
            'author': 'FJS',
            'author_url': 'http://127.0.0.1:8000/FJS',
            'article_time': '2020 年 12 月 21 日',
            'meta_url': 'http://127.0.0.1:8000/default',
            'meta': '默认分类',
            'comment_url': 'http://127.0.0.1:8000/comment',
            'comment_count': '11',
            'abstract': '11',
        },
          {
            'author': 'FJS',
            'author_url': 'http://127.0.0.1:8000/FJS',
            'article_time': '2020 年 12 月 21 日',
            'meta_url': 'http://127.0.0.1:8000/default',
            'meta': '默认分类',
            'comment_url': 'http://127.0.0.1:8000/comment',
            'comment_count': '11',
        },
          {
            'author': 'FJS',
            'author_url': 'http://127.0.0.1:8000/FJS',
            'article_time': '2020 年 12 月 21 日',
            'meta_url': 'http://127.0.0.1:8000/default',
            'meta': '默认分类',
            'comment_url': 'http://127.0.0.1:8000/comment',
            'comment_count': '11',
        },
          {
            'author': 'FJS',
            'author_url': 'http://127.0.0.1:8000/FJS',
            'article_time': '2020 年 12 月 21 日',
            'meta_url': 'http://127.0.0.1:8000/default',
            'meta': '默认分类',
            'comment_url': 'http://127.0.0.1:8000/comment',
            'comment_count': '11',
        },
        {
            'author': 'FJS',
            'author_url': 'http://127.0.0.1:8000/FJS',
            'article_time': '2020 年 12 月 21 日',
            'meta_url': 'http://127.0.0.1:8000/default',
            'meta': '默认分类',
            'comment_url': 'http://127.0.0.1:8000/comment',
            'comment_count': '11',
        },

    ]
    return render(request, "Page/test.html", locals())
