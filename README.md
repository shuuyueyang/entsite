#### 一、entsite项目介绍
计划开发一个企业站点框架，可以基于这个框架，快速搭建不同的企业站点。


#### 二、开发语言环境
* Python 3.8.9
* Django 3.2.6
* Bootstrap 4.6.0
* JQuery
* 2.1 虚拟环境命令：python -m venv entsite
* 2.2 下载代码：git clone https://github.com/shuuyueyang/entsite.git entsite_github
* 2.3 pip 安装包：
      asgiref         3.4.1
      Django          3.2.6
      django-ckeditor 6.1.0
      django-js-asset 1.2.2
      Pillow          8.3.1
      pip             20.2.3
      pytz            2021.1
      setuptools      49.2.1
      sqlparse        0.4.1
      whitenoise      5.3.0
	  django-simple-captcha  0.5.14
* 2.4 python manage.py migrate
* 2.5 python manage.py createsuperuser

#### 三、开发命名规则
* APP名称
* 函数名：小写单词，多个单词以下划线“_”连接
* 类名：首字母大写单词连接组成
