from django import forms

from .models import OnlineMessage

class OnlineMessageForm(forms.ModelForm):
    class Meta:  
        model = OnlineMessage
        fields = ['name','phone','message']