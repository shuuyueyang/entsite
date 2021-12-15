from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from cases.models import OurCases

def index(request):
    cases = OurCases.objects.filter(show_home=True)

    context = {
        'page_id':0,
        'latest_question_list': 'abcd',
        'cases':cases,
    }
    return render(request, 'home/index.html', context)