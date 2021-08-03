from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'msg': 'hello about home',
    }
    return render(request, 'about/index.html', context)