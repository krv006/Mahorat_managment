from django.contrib import admin
from parler.admin import TranslatableAdmin

from core.models import News, NewsImage, Expert, ExpertWebsite, Partner, Project, Employee, Message


class Base(admin.ModelAdmin):
    exclude = "id",


class NewsImageAdmin(admin.StackedInline):
    model = NewsImage
    extra = 1
    exclude = "id",


@admin.register(News)
class NewsAdmin(TranslatableAdmin):
    exclude = "id",
    inlines = NewsImageAdmin,


class ExpertWebsiteAdmin(admin.StackedInline):
    model = ExpertWebsite
    can_delete = False
    max_num = 1


@admin.register(Expert)
class ExpertAdmin(TranslatableAdmin):
    exclude = "website", "id"
    inlines = ExpertWebsiteAdmin,


@admin.register(Partner)
class PartnerAdmin(Base):
    pass


@admin.register(Project)
class ProjectAdmin(TranslatableAdmin):
    exclude = "id",


@admin.register(Message)
class MessageAdmin(Base):
    pass
