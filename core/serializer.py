from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from core.models import Partner, News, Project, NewsImage


class PartnerSerializer(ModelSerializer):
    class Meta:
        model = Partner
        fields = "image", 'url'


class ImageSerializer(ModelSerializer):
    class Meta:
        model = NewsImage
        exclude = "updated_at", "created_at"


class NewsListSerializer(ModelSerializer):
    first_image = SerializerMethodField()

    class Meta:
        model = News
        exclude = ('description',)

    def get_first_image(self, obj):
        first_image = obj.images.first()
        if first_image:
            return ImageSerializer(first_image).data
        return None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = [representation.pop('first_image')]
        return representation


class NewsRetrieveSerializer(ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = News
        exclude = "created_at", "updated_at"


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = "title", "description", "image"
