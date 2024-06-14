from django.utils import translation
from django.utils.text import Truncator
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from parler.forms import TranslatedField
from core.models import Partner, News, Project, NewsImage, Expert, ExpertWebsite, Service, AboutUs, OurWorks, Message, \
    Employee, Country, Study


class PartnerSerializer(ModelSerializer):
    class Meta:
        model = Partner
        fields = "image", 'url'


class ImageSerializer(ModelSerializer):
    class Meta:
        model = NewsImage
        exclude = "updated_at", "created_at"


# class NewsListSerializer(ModelSerializer):
#     first_image = SerializerMethodField()
#
#     class Meta:
#         model = News
#         fields = "__all__"
#
#     def get_first_image(self, obj):
#         first_image = obj.images.first()
#         if first_image:
#             return ImageSerializer(first_image).data
#         return None
#
#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['image'] = [representation.pop('first_image')]
#         return representation
class NewsListSerializer(ModelSerializer):
    title = TranslatedField(read_only=True)
    description = TranslatedField(read_only=True)
    first_image = SerializerMethodField()

    class Meta:
        model = News
        exclude = 'id',

    def get_first_image(self, obj):
        first_image = obj.images.first()
        if first_image:
            return ImageSerializer(first_image).data
        return None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        current_language = translation.get_language()

        if current_language:
            translated_object = instance.translations.get(language_code=current_language)
            if translated_object:
                data['title'] = translated_object.title
                data['description'] = translated_object.description
            data['image'] = [data.pop('first_image')]
        return data


class NewsRetrieveSerializer(ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = News
        exclude = "created_at", "updated_at"


class ProjectSerializer(ModelSerializer):
    title = TranslatedField(read_only=True)
    description = TranslatedField(read_only=True)

    class Meta:
        model = Project
        fields = "title", "description", "image"

    # class ProjectDetailSerializer(ModelSerializer):
    #     description = SerializerMethodField()
    #
    #     class Meta:
    #         model = Project
    #         fields = ['image', 'title', 'description']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        current_language = translation.get_language()

        if current_language:
            translated_object = instance.translations.get(language_code=current_language)
            if translated_object:
                data['title'] = translated_object.title
                data['description'] = translated_object.description
        return data

    def get_description(self, obj):
        description = obj.description
        truncated_description = Truncator(description).words(20)
        return truncated_description


class ExpertWebsiteSerializer(ModelSerializer):
    class Meta:
        model = ExpertWebsite
        fields = "facebook", "linkedin", "messenger"


class ExpertSerializer(ModelSerializer):
    full_name = TranslatedField(read_only=True)
    description = TranslatedField(read_only=True)
    job = TranslatedField(read_only=True)
    websites = ExpertWebsiteSerializer(required=True)

    class Meta:
        model = Expert
        exclude = "id",


    def to_representation(self, instance):
        data = super().to_representation(instance)
        current_language = translation.get_language()

        if current_language:
            translated_object = instance.translation.get(language_code=current_language)
            if translated_object:
                data['full_name'] = translated_object.full_name
                data['description'] = translated_object.description
                data['job'] = translated_object.job
        return data


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        exclude = "id",


class AboutUsSerializer(ModelSerializer):
    class Meta:
        model = AboutUs
        exclude = "id",


class OurWorksSerializer(ModelSerializer):
    title = TranslatedField(read_only=True)
    description = TranslatedField(read_only=True)

    class Meta:
        model = OurWorks
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        current_language = translation.get_language()

        if current_language:
            translated_object = instance.translations.get(language_code=current_language)
            if translated_object:
                data['title'] = translated_object.title
                data['description'] = translated_object.description
            data['image'] = [data.pop('first_image')]
        return data


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        exclude = "id",


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        exclude = "id",


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class StudySerializer(ModelSerializer):
    class Meta:
        model = Study
        fields = "__all__"
