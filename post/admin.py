from django.contrib import admin

# Register your models here.
from post.models import Job, MyHistory


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date', 'price']
    list_display_links = ['title', ]
    save_on_top = True
    list_per_page = 5
    search_fields = ['title']


@admin.register(MyHistory)
class MyHistoryAdmin(admin.ModelAdmin):
    list_display = ['date', 'description', 'name']
    list_display_links = ['date', ]
    save_on_top = True
    list_per_page = 5
    search_fields = ['date']
