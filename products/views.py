from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'page_id': 1,
        'msg': 'hello products home',
    }
    return render(request, 'products/index.html', context)