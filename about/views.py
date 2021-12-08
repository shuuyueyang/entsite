from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'page_id': 3,
        'msg': 'hello about home',
    }
    return render(request, 'about/index.html', context)