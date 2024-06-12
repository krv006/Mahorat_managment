from django.utils.text import Truncator
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from core.models import Partner, News, Project, NewsImage, Expert, ExpertWebsite, Service, AboutUs, OurWorks, Message, \
    Employee


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
<<<<<<< Updated upstream

    # class ProjectDetailSerializer(ModelSerializer):
    #     description = SerializerMethodField()
    #
    #     class Meta:
    #         model = Project
    #         fields = ['image', 'title', 'description']

    def get_description(self, obj):
        description = obj.description
        truncated_description = Truncator(description).words(20)
        return truncated_description


class ExpertWebsiteSerializer(ModelSerializer):
    class Meta:
        model = ExpertWebsite
        fields = "facebook", "linkedin", "messenger"


class ExpertSerializer(ModelSerializer):
    websites = ExpertWebsiteSerializer(required=True)

    class Meta:
        model = Expert
        exclude = "id", "website"


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        exclude = "id",


class AboutUsSerializer(ModelSerializer):
    class Meta:
        model = AboutUs
        exclude = "id",


class OurWorksSerializer(ModelSerializer):
    class Meta:
        model = OurWorks
        fields = "__all__"


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        exclude = "id",


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        exclude = "id",
=======
>>>>>>> Stashed changes
