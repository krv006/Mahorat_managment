from django.urls import path

from core.views import PartnerListAPIView, NewsListAPIView, ProjectListAPIView, NewsRetrieveAPIView, ExpertListAPIView, \
    ServiceListAPIView, ProjectDetailsAPIListView, AboutUsListAPIView, OurWorksListAPIView, MessageListAPIView, \
    EmployeeListAPIView

urlpatterns = [
    path("news/<uuid:pk>", NewsRetrieveAPIView.as_view()),
    path("news/", NewsListAPIView.as_view()),
    path("partners/", PartnerListAPIView.as_view()),
    path("projects/", ProjectListAPIView.as_view()),
    path("project-details/", ProjectDetailsAPIListView.as_view()),

    path("experts/", ExpertListAPIView.as_view()),
    path("services/", ServiceListAPIView.as_view()),

    path("about-us/", AboutUsListAPIView.as_view()),
    path("our-works/", OurWorksListAPIView.as_view()),

    path("message/", MessageListAPIView.as_view()),
    path("emplyee/", EmployeeListAPIView.as_view()),
]
