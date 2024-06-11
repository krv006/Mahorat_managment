<<<<<<< HEAD
from django.utils.text import Truncator
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
=======
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
>>>>>>> ef18812b7247eac6e4355ec9d6b34ff93ba7b7c5

from core.models import Partner, News, Project, Expert, Service, AboutUs, OurWorks, Message, Employee
from core.serializer import PartnerSerializer, NewsListSerializer, ProjectSerializer, NewsRetrieveSerializer, \
    ExpertSerializer, ServiceSerializer, AboutUsSerializer, OurWorksSerializer, MessageSerializer, EmployeeSerializer


class BaseTruncateDescriptionMixin:
    def truncate_description(self, queryset):
        for item in queryset:
            item.description = Truncator(item.description).chars(400)
        return queryset


class PartnerListAPIView(ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer


class NewsRetrieveAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsRetrieveSerializer


class ProjectListAPIView(BaseTruncateDescriptionMixin, ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetailsAPIListView(BaseTruncateDescriptionMixin, ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return self.truncate_description(qs)


class ExpertListAPIView(ListAPIView):
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer


class ServiceListAPIView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class AboutUsListAPIView(ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class OurWorksListAPIView(ListAPIView):
    queryset = OurWorks.objects.all()
    serializer_class = OurWorksSerializer


class MessageListAPIView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class EmployeeListAPIView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# class PartnerListAPIView(ListAPIView):
#     queryset = Partner.objects.all()
#     serializer_class = PartnerSerializer
#
#
# class NewsListAPIView(ListAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsListSerializer
#
#
# class NewsRetrieveAPIView(RetrieveAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsRetrieveSerializer
#
#
# class ProjectListAPIView(ListAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
#
#
# class ProjectDetailsAPIListView(ListAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#         for project in qs:
#             project.description = Truncator(project.description).words(40)
#         return qs
#
#
# class ExpertListAPIView(ListAPIView):
#     queryset = Expert.objects.all()
#     serializer_class = ExpertSerializer
#
#
# class ServiceListAPIView(ListAPIView):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer
#
#
# class AboutUsListAPIView(ListAPIView):
#     queryset = AboutUs.objects.all()
#     serializer_class = AboutUsSerializer
#
#
# class OurWorksListAPIView(ListAPIView):
#     queryset = OurWorks.objects.all()
#     serializer_class = OurWorksSerializer
