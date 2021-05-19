from django.urls import path

from . import views

urlpatterns = [
    path('<int:news_id>/', views.detail, name='detail'),
]