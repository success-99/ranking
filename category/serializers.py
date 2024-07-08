from rest_framework import serializers
from .models import TotalDoc, CategoryOne, SubCategoryTwoFile, CategoryTwo, SubCategoryTwo, SubCategoryTwoUser, \
    CategoryOneUser, TotalDocUser, CategoryTwoUser
import os


# TotalDoc model serializers
class TotalDocListModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = TotalDoc
        fields = ['id', 'title']


# TotalDocUser model serializers
class TotalDocUserListModelSerializers(serializers.ModelSerializer):
    student = serializers.CharField(source='student.user.get_full_name')
    title = serializers.CharField(source='title.title')

    class Meta:
        model = TotalDocUser
        fields = ['id', 'student', 'title', 'mark', 'short_description']


class TotalDocUserTeacherMarkShortDescriptionCreateModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = TotalDocUser
        fields = ['id', 'student', 'title', 'mark', 'short_description']


# CategoryOne model serializers
class CategoryOneListModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryOne
        fields = ['id', 'title']


# CategoryOneUser model serializers
class CategoryOneUserListModelSerializers(serializers.ModelSerializer):
    student = serializers.CharField(source='student.user.get_full_name')
    title = serializers.CharField(source='title.title')

    class Meta:
        model = CategoryOneUser
        fields = ['id', 'student', 'title', 'file', 'mark', 'short_description']


class CategoryOneUserFilterListModelSerializers(serializers.ModelSerializer):
    student = serializers.CharField(source='student.user.get_full_name', read_only=True)
    title = serializers.CharField(source='title.title', read_only=True)

    class Meta:
        model = CategoryOneUser
        fields = ['id', 'student', 'title', 'file', 'mark', 'short_description']


class CategoryOneStudentFileCreateModelSerializers(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = CategoryOneUser
        fields = ['id', 'student', 'title', 'file']


class CategoryOneTeacherMarkShortDescriptionCreateModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryOneUser
        fields = ['id', 'mark', 'short_description']


# CategoryTwo model serializers
class CategoryTwoListModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryTwo
        fields = ['id', 'title']


# CategoryTwoUser model serializers
class CategoryTwoUserListModelSerializers(serializers.ModelSerializer):
    student = serializers.CharField(source='student.user.get_full_name')
    title = serializers.CharField(source='title.title')

    class Meta:
        model = CategoryTwoUser
        fields = ['id', 'student', 'title', 'mark']


# SubCategoryTwo model serializers
class SubCategoryTwoListModelSerializers(serializers.ModelSerializer):
    title = serializers.CharField(source='title.title')

    class Meta:
        model = SubCategoryTwo
        fields = ['id', 'title', 'sub_title']


# SubCategoryTwoUser model serializers
class SubCategoryTwoStudentListModelSerializers(serializers.ModelSerializer):
    student = serializers.CharField(source='student.user.get_full_name')
    sub_title = serializers.CharField(source='sub_title.sub_title')

    class Meta:
        model = SubCategoryTwoUser
        fields = ['id', 'student', 'sub_title', 'mark', 'short_description']


class SubCategoryTwoTeacherUpdateShortDescriptionModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = SubCategoryTwoUser
        fields = ['id', 'student', 'sub_title', 'short_description']


# SubCategoryTwoFile model serializers
class SubCategoryTwoFileStudentFileListModelSerializers(serializers.ModelSerializer):
    student = serializers.CharField(source='student.user.get_full_name')
    sub_title = serializers.CharField(source='sub_title.sub_title')

    class Meta:
        model = SubCategoryTwoFile
        fields = ['id', 'student', 'sub_title', 'file', 'is_approved']


class SubCategoryTwoFileStudentFilterListModelSerializers(serializers.ModelSerializer):
    student = serializers.CharField(source='student.user.get_full_name', read_only=True)
    sub_title = serializers.CharField(source='sub_title.sub_title', read_only=True)

    class Meta:
        model = SubCategoryTwoFile
        fields = ['id', 'student', 'sub_title', 'file']


class SubCategoryTwoFileStudentFileCreateModelSerializers(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = SubCategoryTwoFile
        fields = ['id', 'student', 'sub_title', 'file']


class SubCategoryTwoFileTeacherIsApprovedUpdateModelSerializers(serializers.ModelSerializer):
    is_approved = serializers.BooleanField(default=False)

    class Meta:
        model = SubCategoryTwoFile
        fields = ['id', 'is_approved']


# class CategoryTwoModelSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = CategoryTwo
#         fields = ['id', 'title']
#
#
# class SubCategoryTwoModelSerializers(serializers.ModelSerializer):
#     title = serializers.CharField(source='title.title')
#
#     class Meta:
#         model = SubCategoryTwo
#         fields = ['id', 'title', 'sub_title']
#
#
# class SubCategoryTwoFileModelSerializers(serializers.ModelSerializer):
#     title = serializers.CharField(source='title.title')
#     student = serializers.CharField(source='student.user.get_full_name')
#
#     class Meta:
#         model = SubCategoryTwoFile
#         fields = ['id', 'title', 'student', 'file', 'is_approved']
#
#
# class CategoryOneTeacherStudentMarkModelSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = CategoryOneUser
#         fields = ['mark']
#
#
# class CategoryOneStudentModelSerializers(serializers.ModelSerializer):
#     file = serializers.FileField()
#
#     class Meta:
#         model = CategoryOne
#         fields = ['file']
#
#     def validate_file(self, value):
#         valid_extensions = ['.pdf', '.jpg', '.png', '.jpeg']
#         ext = os.path.splitext(value.name)[1]
#         if not ext.lower() in valid_extensions:
#             raise serializers.ValidationError("Fayl .pdf, .jpg, .png .jpeg turidan birida bo'lishi kerak")
#         return value
#
#
# class SubCategoryTwoFileStudentModelSerializers(serializers.ModelSerializer):
#     file = serializers.FileField()
#
#     class Meta:
#         model = SubCategoryTwoFile
#         fields = ['title', 'file', 'student']
#         extra_kwargs = {
#             'is_approved': {'required': False}
#
#         }
#
#     def validate_file(self, value):
#         valid_extensions = ['.pdf', '.jpg', '.png', '.jpeg']
#         ext = os.path.splitext(value.name)[1]
#         if not ext.lower() in valid_extensions:
#             raise serializers.ValidationError("Fayl .pdf, .jpg, .png .jpeg turidan birida bo'lishi kerak")
#         return value
#
#
class CombinedTitleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    source = serializers.CharField(max_length=50)

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
