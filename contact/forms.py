from django import forms
from captcha.fields import CaptchaField

from .models import OnlineMessage

class OnlineMessageForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:  
        model = OnlineMessage
        fields = ['name','phone','message']