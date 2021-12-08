from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'page_id': 2,
        'msg': 'hello cases home',
    }
    return render(request, 'cases/index.html', context)