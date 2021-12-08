from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    context = {
        'page_id':0,
        'latest_question_list': 'abcd',
    }
    return render(request, 'home/index.html', context)