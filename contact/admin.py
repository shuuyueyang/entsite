from django.contrib import admin

# Register your models here.
from contact.models import OnlineMessage

class OnlineMessageAdmin(admin.ModelAdmin):
    list_display = ['name','phone','message','_created_date']
    fields = ('name','phone','message')
    list_filter = ('name','phone','message')

admin.site.register(OnlineMessage, OnlineMessageAdmin)
