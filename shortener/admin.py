from django.contrib import admin

from shortener.models import Url

@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ['url', 'url_short']
    list_display_links = ['url', 'url_short']
    readonly_fields = ('date_create',)
