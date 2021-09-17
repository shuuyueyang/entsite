import json
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, View
from django.shortcuts import HttpResponse,get_object_or_404

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
    def post(self, request, *args, **kwargs):
        res = dict(result=False)
        form = self.get_form()
        if form.is_valid():
            form.save()
            res['result'] = True
        else:
            pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
            form_errors = str(form.errors)
            errors = re.findall(pattern, form_errors)
            res['error'] = errors[0]
        return HttpResponse(json.dumps(res), content_type='application/json')