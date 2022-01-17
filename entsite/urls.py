"""entsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path,re_path
from django.conf import settings
from django.conf.urls.static import static
from  django.views.static import serve
from .settings import MEDIA_ROOT

from django.contrib.sitemaps.views import sitemap
from .sitemaps import sitemaps

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    path('', include('home.urls')),
    path('cases/', include('cases.urls')),
    path('contact/', include('contact.urls')),
    path('news/', include('news.urls')),
    path('about/', include('about.urls')),
    path('products/', include('products.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('captcha/', include('captcha.urls')),
    re_path(r'^media/(?P<path>.*)$',serve,{'document_root': MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
