from django.db import models
from common.models import MetaData, TimeStamped

from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import  RichTextUploadingField

# Create your models here.
class OnlineMessage(TimeStamped):

    name = models.CharField(_('name'), max_length=255, default=_(''))
    phone = models.CharField(_('phone'), max_length=255, default=_(''))

    message = models.TextField(_('message'), blank=True)
    
    def __str__(self):
        return self.message
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name = _('OnlineMessage')
        verbose_name_plural = _('在线留言')