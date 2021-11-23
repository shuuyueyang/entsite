from django.http import Http404
from django.shortcuts import render

# Create your views here.

from .models import News
from .models import Category
# ...
def index(request):
    categories = Category.objects.all()
    news = News.objects.all()
    context = {
        'msg': 'hello news home',
        'categories':categories,
        'news': news
    }
    return render(request, 'news/index.html', context)
def detail(request, news_id):
    try:
        news = News.objects.get(pk=news_id)
    except News.DoesNotExist:
        raise Http404("news does not exist")
    return render(request, 'news/detail.html', {'news': news})
