from django.db import models
from common.models import MetaData, TimeStamped

from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import  RichTextUploadingField

# Create your models here.
# 企业站的新闻页
# News的字段包括：
# 新闻标题 title
# 新闻图片（每个新闻关联一个图片）image
# 正文 content
# 状态（草稿、发布） status
# 发布日期publication_date
# News的属性包括：
# is_visible是否能在前端网页显示
DRAFT = 0
HIDDEN = 1
PUBLISHED = 2

class Category(TimeStamped):

    seq_number =  models.IntegerField(_('seq_number'))

    name = models.CharField(_('name'), max_length=255, default=_(''))

    slug = models.SlugField(_('slug'), unique=True, max_length=255, help_text=_("Used to build the category's URL."))

    description = models.TextField(_('description'), blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('新闻栏目管理')

class News(MetaData, TimeStamped):
    STATUS_CHOICES = ((DRAFT, _('draft')),
                      (HIDDEN, _('hidden')),
                      (PUBLISHED, _('published')))
    
    title = models.CharField(
        _('title'), max_length=255)
        
    avatar = models.ImageField(upload_to='news/%Y%m%d/', blank=True)
        
    content = RichTextUploadingField()#RichTextField()    #models.TextField(_('content'), blank=True)
    
    category = models.ForeignKey(Category, verbose_name = _('category'), on_delete=models.SET_NULL, null=True, blank=True,)
    
    status = models.IntegerField(
        _('status'), db_index=True,
        choices=STATUS_CHOICES, default=DRAFT)

    publication_date = models.DateTimeField(
        _('publication date'),
        db_index=True, default=timezone.now,
        help_text=_("Used to build the entry's URL."))
        
    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
    @property
    def is_visible(self):
        """
        Checks if an entry is visible and published.
        """
        return self.is_actual and self.status == PUBLISHED
    
    class Meta:
        verbose_name = _('news')
        verbose_name_plural = _('新闻管理')