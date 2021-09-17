from django.urls import path

from . import views

app_name="contact"

urlpatterns = [
    path('', views.index, name='index'),
    path('contact_create_message', views.OnlineMessageCreateView.as_view(), name='OnlineMessageCreateView'),
]