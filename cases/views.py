from django.core.paginator import Paginator
from django.shortcuts import render

from .models import OurCases
from django.shortcuts import HttpResponse


# Create your views here.

#将所有的成功案例分页显示，目前每页显示8个
def index(request):

    ourCases=OurCases.objects.all()
    pages=Paginator(ourCases,8)
    p = pages.page(1)
    context = {
        'page_id': 2,
        'page':p,
    }
    return render(request, 'cases/index.html', context)

# 返回第几页数据
def page(request,page_num=1):

    ourCases=OurCases.objects.all()
    pages=Paginator(ourCases,8)
    p=pages.page(int(page_num))
    context = {
        'page_id': 2,
        'page':p,
    }
    return render(request, 'cases/index.html', context)

#根据案例的id返回某个案例

def caseshow(request,case_id=1):
    '''
    try:
        news = News.objects.get(pk=news_id)
    except News.DoesNotExist:
        raise Http404("news does not exist")

    '''
    cs=OurCases.objects.filter(id=int(case_id))[0]

    context = {
        'page_id': 2,
        'case':cs,
    }
    return render(request, 'cases/caseshow.html', context)
