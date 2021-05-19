from django.contrib import admin

# Register your models here.
from news.models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','content','status','publication_date']
    fields = ('title','avatar','content','status','publication_date','category','_meta_keywords','_meta_description')
    list_filter = ('title','content','status','publication_date')
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','seq_number','slug','description']
    fields = ('name','seq_number','slug','description')
    list_filter = ('name','seq_number','slug','description')

#admin.site.register(News)
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
