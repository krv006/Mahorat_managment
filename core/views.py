from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from core.models import Partner, News, Project
from core.serializer import PartnerSerializer, NewsListSerializer, ProjectSerializer, NewsRetrieveSerializer


class PartnerListAPIView(ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer


class NewsRetrieveAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsRetrieveSerializer


class ProjectListAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
