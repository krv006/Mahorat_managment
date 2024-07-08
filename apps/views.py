from django.utils import translation
from django.utils.text import Truncator
from drf_yasg.openapi import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from apps.models import Partner, News, Project, Expert, Service, AboutUs, OurWorks, Message, Employee, Country, Study
from apps.serializer import PartnerSerializer, NewsListSerializer, ProjectSerializer, NewsRetrieveSerializer, \
    ExpertSerializer, ServiceSerializer, AboutUsSerializer, OurWorksSerializer, MessageSerializer, EmployeeSerializer, \
    CountrySerializer, StudySerializer
from apps.tasks import send_email
from root.settings import EMAIL_HOST_USER


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

    def get_queryset(self):
        queryset = super().get_queryset()

        user_language = translation.get_language()
        if user_language:
            queryset = queryset.filter(translations__language_code=user_language)

        return queryset


class NewsRetrieveAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsRetrieveSerializer


class ProjectListAPIView(BaseTruncateDescriptionMixin, ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        user_language = translation.get_language()
        if user_language:
            queryset = queryset.filter(translations__language_code=user_language)

        return queryset


class ProjectDetailsAPIListView(BaseTruncateDescriptionMixin, ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        user_language = translation.get_language()
        if user_language:
            queryset = queryset.filter(translations__language_code=user_language)

        return queryset


class ExpertListAPIView(ListAPIView):
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        user_language = translation.get_language()
        if user_language:
            queryset = queryset.filter(translation__language_code=user_language)

        return queryset


class ServiceListAPIView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        user_language = translation.get_language()
        if user_language:
            queryset = queryset.filter(translations__language_code=user_language)

        return queryset


class AboutUsListAPIView(ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        user_language = translation.get_language()
        if user_language:
            queryset = queryset.filter(translations__language_code=user_language)

        return queryset


class OurWorksListAPIView(ListAPIView):
    queryset = OurWorks.objects.all()
    serializer_class = OurWorksSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        user_language = translation.get_language()
        if user_language:
            queryset = queryset.filter(translations__language_code=user_language)

        return queryset


class MessageCreateAPIView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class EmployeeCreateAPIView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def post(self, request, *args, **kwargs):
        data = super().post(request, *args, **kwargs)
        message = (f"Yangi ishchi:\nIsmi: {data.data['first_name']},\nFamiliyasi: {data.data['last_name']}\n"
                   f"Email adresi: {data.data['email']}\nTelefon raqami: {data.data['phone_number']}\n"
                   f"Tili: {data.data['language']}\nTajribasi: {data.data['experience']}\n"
                   f"Shaxsi: {data.data['title']}\nIsh davomiyligi: {data.data['duration']}\n"
                   f"Xabar: {data.data['special_request']}\nDavlati: {Country.objects.get(pk=data.data['country'])}\n"
                   f"Ta'lim yo'nalishi: {Study.objects.get(pk=data.data['study'])}")

        send_email.delay(EMAIL_HOST_USER, message)
        return data


class CountryListAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class StudyListAPIView(ListAPIView):
    queryset = Study.objects.all()
    serializer_class = StudySerializer
