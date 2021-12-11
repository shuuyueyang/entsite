from django.urls import path

from . import views

app_name="cases"

urlpatterns = [
    path('', views.index, name='index'),

    #成功案例翻页按钮
    path('<int:page_num>',views.page, name='case_page'),


    #成功案例详情页
    path('caseshow/<int:case_id>',views.caseshow, name='detail_page'),
]