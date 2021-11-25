from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'msg': 'hello cases home',
    }
    return render(request, 'cases/index.html', context)