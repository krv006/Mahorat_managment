from django.contrib import admin

from core.models import News, NewsImage, Expert, ExpertWebsite, Partner, Project, Employee


class Base(admin.ModelAdmin):
    exclude = "id",


class NewsImageAdmin(admin.StackedInline):
    model = NewsImage
    extra = 1
    exclude = "id",


@admin.register(News)
class NewsAdmin(Base):
    inlines = NewsImageAdmin,


class ExpertWebsiteAdmin(admin.StackedInline):
    model = ExpertWebsite
    can_delete = False
    max_num = 1


@admin.register(Expert)
class ExpertAdmin(Base):
    exclude = "website",
    inlines = ExpertWebsiteAdmin,


@admin.register(Partner)
class PartnerAdmin(Base):
    pass


@admin.register(Project)
class ProjectAdmin(Base):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass

