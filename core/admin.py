from django.contrib import admin

from core.models import News, NewsImage


class NewsImageAdmin(admin.StackedInline):
    exclude = 'id',
    model = NewsImage
    extra = 1


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    exclude = 'id',
    inlines = NewsImageAdmin,
