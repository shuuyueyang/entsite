from django.http import Http404
from django.shortcuts import render

# Create your views here.

from .models import News
# ...
def index(request):
    context = {
        'msg': 'hello news home',
    }
    return render(request, 'news/index.html', context)
def detail(request, news_id):
    try:
        news = News.objects.get(pk=news_id)
    except News.DoesNotExist:
        raise Http404("news does not exist")
    return render(request, 'news/detail.html', {'news': news})
