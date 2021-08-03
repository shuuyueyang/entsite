from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'msg': 'hello products home',
    }
    return render(request, 'products/index.html', context)