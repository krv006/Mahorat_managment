from django.urls import path

from core.views import PartnerListAPIView, NewsListAPIView, ProjectListAPIView, NewsRetrieveAPIView

urlpatterns = [
    path("news/<uuid:pk>", NewsRetrieveAPIView.as_view()),
    path("news/", NewsListAPIView.as_view()),
    path("partner/", PartnerListAPIView.as_view()),
    path("projects/", ProjectListAPIView.as_view()),
]
