from django.contrib.sitemaps import Sitemap
from cases.models import OurCases

from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'never'
    protocol = 'https'

    def items(self):
        return ['home:index', 'products:index', 'about:index', 'cases:index']

    def location(self, item):
        return reverse(item)

class CaseSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5
    protocol = 'https'

    def items(self):
        return OurCases.objects.all()

    # def lastmod(self, obj):
        # return obj.pub_date
    def location(self, obj):#可选.返回每个对象的绝对路径.如果对象有get_absolute_url()方法,可以省略location
        return reverse('cases:detail_page', kwargs={'case_id': obj.id})
        
sitemaps = {
    'case': CaseSitemap,
    'staticview':StaticViewSitemap,
}