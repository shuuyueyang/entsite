from django.db import models
from common.models import MetaData


# Create your models here.
class OurCases(models.Model):
    #网站的title
    title = models.CharField(max_length=100)

    #在成功案例页面所展示的图片的url
    img_url = models.CharField(max_length=100,default='#')

    #详细信息，页面的一些信息
    detail = models.TextField(max_length=3000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '成功案例'
        verbose_name_plural = '成功案例'
