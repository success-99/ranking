from rest_framework import serializers
from .models import TotalDoc, CategoryOne, SubCategoryTwoFile, CategoryTwo, SubCategoryTwo
import os


class TotalDocModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = TotalDoc
        fields = ['id', 'title', 'mark']


class TotalDocTeacherModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = TotalDoc
        fields = ['mark']
        extra_kwargs = {
            'title': {'required': False}
        }


class CategoryOneModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryOne
        fields = ['id', 'title', 'file', 'mark']


class CategoryTwoModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryTwo
        fields = ['id', 'title', 'marks']


class SubCategoryTwoModelSerializers(serializers.ModelSerializer):
    title = serializers.CharField(source='title.title')

    class Meta:
        model = SubCategoryTwo
        fields = ['id', 'title', 'sub_title', 'mark']


class SubCategoryTwoFileModelSerializers(serializers.ModelSerializer):
    title = serializers.CharField(source='title.title')
    student = serializers.CharField(source='student.user.get_full_name')

    class Meta:
        model = SubCategoryTwoFile
        fields = ['id', 'title', 'student', 'file', 'is_approved']


class CategoryOneTeacherModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryOne
        fields = ['mark']


class CategoryOneStudentModelSerializers(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = CategoryOne
        fields = ['file']

    def validate_file(self, value):
        valid_extensions = ['.pdf', '.jpg', '.png', '.jpeg']
        ext = os.path.splitext(value.name)[1]
        if not ext.lower() in valid_extensions:
            raise serializers.ValidationError("Fayl .pdf, .jpg, .png .jpeg turidan birida bo'lishi kerak")
        return value


class SubCategoryTwoFileStudentModelSerializers(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = SubCategoryTwoFile
        fields = ['file']

    def validate_file(self, value):
        valid_extensions = ['.pdf', '.jpg', '.png', '.jpeg']
        ext = os.path.splitext(value.name)[1]
        if not ext.lower() in valid_extensions:
            raise serializers.ValidationError("Fayl .pdf, .jpg, .png .jpeg turidan birida bo'lishi kerak")
        return value

#         # depth = 1
#
#
# class TitleFileModelSerializers(serializers.ModelSerializer):
#     file = serializers.FileField(required=False)
#     status = serializers.BooleanField(default=False)
#
#     class Meta:
#         model = TitleFile
#         fields = ['id', 'student', 'title', 'file', 'description', 'status']
#         extra_kwargs = {
#             'student': {'required': False},
#             'title': {'required': False}
#
#         }
#         # depth = 1
#
# def validate_file(self, value):
#     valid_extensions = ['.pdf', '.jpg', '.png', '.jpeg']
#     ext = os.path.splitext(value.name)[1]
#     if not ext.lower() in valid_extensions:
#         raise serializers.ValidationError("Fayl .pdf, .jpg, .png .jpeg turidan birida bo'lishi kerak")
#     return value
#
