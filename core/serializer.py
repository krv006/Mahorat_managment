from rest_framework.serializers import ModelSerializer

from core.models import Partner, News, Project


class PartnerSerializer(ModelSerializer):
    class Meta:
        model = Partner
        fields = "image", 'url'


class ImageSerializer(ModelSerializer):
    pass


class NewsListSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class NewsRetrieveSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = "image", 'description', 'created_at', 'title'
