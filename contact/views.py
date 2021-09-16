from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'msg': 'hello contact home',
    }
    return render(request, 'contact/index.html', context)