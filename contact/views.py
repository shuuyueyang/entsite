import json
import re
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, View
from django.shortcuts import HttpResponse,get_object_or_404
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url

from .models import OnlineMessage
from .forms import OnlineMessageForm
# Create your views here.
def index(request):
    context = {
        'msg': 'hello contact home',
    }
    return render(request, 'contact/index.html', context)

class OnlineMessageCreateView(CreateView):
    model = OnlineMessage
    fields = '__all__'
    def get(self, request, *args, **kwargs):
        print("enter!")
        #form = self.get_form()
        form = OnlineMessageForm()
        return render(request,'contact/onlinemessage_form.html',context={'form':form})
    def post(self, request, *args, **kwargs):
        res = dict(result=False)
        form = OnlineMessageForm(request.POST)#self.get_form()
        if form.is_valid():
            form.save()
            res['result'] = True
        else:
            print(form.errors)
            res['errors'] = form.errors.as_json()
        return HttpResponse(json.dumps(res), content_type='application/json')
def test_captcha(request):
    if request.method == "POST":
        form = OnlineMessageForm(request.POST)
        print(form)
        res = dict(result=False)
        if form.is_valid():
            form.save()
            res['result'] = True
            return render(request,'contact/test_captcha.html',context={'form':form})
        else:
            res['result'] = False
            res['errors'] = form.errors
            return HttpResponse(json.dumps(res), content_type='application/json')
            #print("has errors")
            #print(form.errors)
            #return render(request,'contact/test_captcha.html',context={'form':form})
    else:
        form = OnlineMessageForm()
        return render(request,'contact/test_captcha.html',context={'form':form})