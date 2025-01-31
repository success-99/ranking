from django.db import transaction
from rest_framework import status, parsers, mixins, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TotalDocListModelSerializers, TotalDocUserTeacherMarkShortDescriptionCreateModelSerializers, \
    TotalDocUserListModelSerializers, CategoryOneListModelSerializers, CategoryOneUserListModelSerializers, \
    CategoryOneStudentFileCreateModelSerializers, CategoryOneTeacherMarkShortDescriptionCreateModelSerializers, CombinedTitleSerializer, \
    CategoryTwoListModelSerializers, CategoryTwoUserListModelSerializers, SubCategoryTwoListModelSerializers, \
    SubCategoryTwoStudentListModelSerializers, SubCategoryTwoFileStudentFileCreateModelSerializers, \
    SubCategoryTwoFileStudentFileListModelSerializers, SubCategoryTwoFileTeacherIsApprovedUpdateModelSerializers, \
    CategoryOneUserFilterListModelSerializers, SubCategoryTwoFileStudentFilterListModelSerializers, \
    SubCategoryTwoTeacherUpdateShortDescriptionModelSerializers, CategoryOneUserSerializer

from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.pagination import LimitOffsetPagination
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action, api_view, permission_classes
from .models import TotalDoc, CategoryOne, SubCategoryTwoFile, CategoryTwo, SubCategoryTwo, TotalDocUser, \
    CategoryOneUser, CategoryTwoUser, SubCategoryTwoUser
from users.permissions import IsStudent, IsTeacher, IsSuperAdmin
from django.shortcuts import render


# TotalDoc model views
class TotalDocRetrieveListModelMixinView(mixins.RetrieveModelMixin,
                                         mixins.ListModelMixin,
                                         GenericViewSet):
    permission_classes = (AllowAny,)
    queryset = TotalDoc.objects.all()
    serializer_class = TotalDocListModelSerializers


# TotalDocUser model views
class TotalDocUserRetrieveListModelMixinView(mixins.RetrieveModelMixin,
                                             mixins.ListModelMixin,
                                             GenericViewSet):
    permission_classes = (AllowAny,)
    queryset = TotalDocUser.objects.all()
    serializer_class = TotalDocUserListModelSerializers


class TotalDocTeacherMarkUpdateModelMixinView(mixins.CreateModelMixin,
                                              GenericViewSet):
    queryset = TotalDocUser.objects.all()
    serializer_class = TotalDocUserTeacherMarkShortDescriptionCreateModelSerializers
    http_method_names = ['post']

    def get_permissions(self):
        if self.request.method in ['POST']:
            return [IsTeacher()]
        else:
            return super().get_permissions()





# CategoryOne model views
class CategoryOneRetrieveListModelMixinView(mixins.RetrieveModelMixin,
                                            mixins.ListModelMixin,
                                            GenericViewSet):
    permission_classes = (AllowAny,)
    queryset = CategoryOne.objects.all()
    serializer_class = CategoryOneListModelSerializers


# CategoryOneUser model views
class CategoryOneUserRetrieveListModelMixinView(mixins.RetrieveModelMixin,
                                                mixins.ListModelMixin,
                                                GenericViewSet):
    permission_classes = (AllowAny,)
    queryset = CategoryOneUser.objects.all()
    serializer_class = CategoryOneUserListModelSerializers


@api_view(['GET'])
@permission_classes([IsStudent])
def get_category_one_by_student_and_title(request, student_id, title_id):
    files = CategoryOneUser.objects.filter(student_id=student_id, title_id=title_id)
    serializer = CategoryOneUserFilterListModelSerializers(files, many=True)
    return Response(serializer.data)


class CategoryOneUserAPIView(APIView):
    def get(self, request, id):
        users = CategoryOneUser.objects.filter(title_id=id).select_related('student')
        serialized_users = CategoryOneUserSerializer(users, many=True)  # Agar serialize qilish kerak bo'lsa
        return Response(serialized_users.data)



class CategoryOneStudentFileCreateDeleteModelMixinView(mixins.CreateModelMixin, mixins.DestroyModelMixin,
                                                       GenericViewSet):
    queryset = CategoryOneUser.objects.all()
    serializer_class = CategoryOneStudentFileCreateModelSerializers
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)

    http_method_names = ['post', 'delete']

    def get_permissions(self):
        if self.request.method in ['POST', 'DELETE']:
            return [IsStudent()]
        else:
            return super().get_permissions()


class CategoryOneTeacherUpdateMarkModelMixinView(mixins.UpdateModelMixin,
                                                 GenericViewSet):
    queryset = CategoryOneUser.objects.all()
    serializer_class = CategoryOneTeacherMarkShortDescriptionCreateModelSerializers
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)

    http_method_names = ['patch']

    def get_permissions(self):
        if self.request.method in ['PATCH']:
            return [IsTeacher()]
        else:
            return super().get_permissions()


# CategoryTwo model views
class CategoryTwoRetrieveListModelMixinView(mixins.RetrieveModelMixin,
                                            mixins.ListModelMixin,
                                            GenericViewSet):
    permission_classes = (AllowAny,)
    queryset = CategoryTwo.objects.all()
    serializer_class = CategoryTwoListModelSerializers


# CategoryTwoUser model views
class CategoryTwoUserRetrieveListModelMixinView(mixins.RetrieveModelMixin,
                                                mixins.ListModelMixin,
                                                GenericViewSet):
    permission_classes = (AllowAny,)
    queryset = CategoryTwoUser.objects.all()
    serializer_class = CategoryTwoUserListModelSerializers


class SubCategoryTwoRetrieveListModelMixinView(mixins.RetrieveModelMixin,
                                               mixins.ListModelMixin,
                                               GenericViewSet):
    permission_classes = (AllowAny,)
    queryset = SubCategoryTwo.objects.all()
    serializer_class = SubCategoryTwoListModelSerializers


class SubCategoryTwoStudentRetrieveListModelMixinView(mixins.RetrieveModelMixin,
                                                      mixins.ListModelMixin,
                                                      GenericViewSet):
    permission_classes = (AllowAny,)
    queryset = SubCategoryTwoUser.objects.all()
    serializer_class = SubCategoryTwoStudentListModelSerializers


class SubCategoryTwoTeacherUpdateShortDescriptionModelMixinView(mixins.UpdateModelMixin,
                                                              GenericViewSet):
    queryset = SubCategoryTwoUser.objects.all()
    serializer_class = SubCategoryTwoTeacherUpdateShortDescriptionModelSerializers
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)

    http_method_names = ['patch']

    def get_permissions(self):
        if self.request.method in ['PATCH']:
            return [IsTeacher()]
        else:
            return super().get_permissions()


# SubCategoryTwoFile model view
class SubCategoryTwoFileStudentRetrieveListModelMixinView(mixins.RetrieveModelMixin,
                                                          mixins.ListModelMixin,
                                                          GenericViewSet):
    permission_classes = (AllowAny,)
    queryset = SubCategoryTwoFile.objects.all()
    serializer_class = SubCategoryTwoFileStudentFileListModelSerializers


@api_view(['GET'])
@permission_classes([IsStudent])
def get_subcategory_two_file_by_student_and_title(request, student_id, sub_title_id):
    files = SubCategoryTwoFile.objects.filter(student_id=student_id, sub_title_id=sub_title_id)
    serializer = SubCategoryTwoFileStudentFilterListModelSerializers(files, many=True)
    return Response(serializer.data)


class SubCategoryTwoFileStudentCreateDeleteModelMixinView(mixins.CreateModelMixin, mixins.DestroyModelMixin,
                                                          GenericViewSet):
    queryset = SubCategoryTwoFile.objects.all()
    serializer_class = SubCategoryTwoFileStudentFileCreateModelSerializers
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)

    http_method_names = ['post', 'delete']

    def get_permissions(self):
        if self.request.method in ['POST', 'DELETE']:
            return [IsStudent()]
        else:
            return super().get_permissions()


class SubCategoryTwoFileTeacherIsApprovedUpdateModelMixinView(mixins.UpdateModelMixin,
                                                              GenericViewSet):
    queryset = SubCategoryTwoFile.objects.all()
    serializer_class = SubCategoryTwoFileTeacherIsApprovedUpdateModelSerializers
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)

    http_method_names = ['patch']

    def get_permissions(self):
        if self.request.method in ['PATCH']:
            return [IsTeacher()]
        else:
            return super().get_permissions()


# class CategoryOneTeacherModelViewSet(mixins.UpdateModelMixin,
#                                      GenericViewSet):
#     queryset = CategoryOne.objects.all()
#     serializer_class = CategoryOneTeacherStudentMarkModelSerializers
#     http_method_names = ['patch']
#
#     def get_permissions(self):
#         if self.request.method in ['PATCH']:
#             return [IsAuthenticated()]
#         else:
#             return super().get_permissions()

#
# class CategoryOneStudentModelViewSet(mixins.UpdateModelMixin,
#                                      GenericViewSet):
#     queryset = CategoryOne.objects.all()
#     serializer_class = CategoryOneStudentModelSerializers
#     parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)
#
#     http_method_names = ['patch']
#
#     def get_permissions(self):
#         if self.request.method in ['PATCH']:
#             return [IsAuthenticated()]
#         else:
#             return super().get_permissions()
#
#
# class SubCategoryTwoFileStudentModelViewSet(mixins.CreateModelMixin,
#                                             GenericViewSet):
#     queryset = SubCategoryTwoFile.objects.all()
#     serializer_class = SubCategoryTwoFileStudentModelSerializers
#     parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)
#
#     http_method_names = ['post']
#
#     def get_permissions(self):
#         if self.request.method in ['POST']:
#             return [IsStudent()]
#         else:
#             return super().get_permissions()
#
#
# class CategoryOneModelViewSet(mixins.RetrieveModelMixin,
#                               mixins.ListModelMixin,
#                               GenericViewSet):
#     permission_classes = (AllowAny,)
#     queryset = CategoryOne.objects.all()
#     serializer_class = CategoryOneModelSerializers
#
#
# class CategoryTwoModelViewSet(mixins.RetrieveModelMixin,
#                               mixins.ListModelMixin,
#                               GenericViewSet):
#     permission_classes = (AllowAny,)
#     queryset = CategoryTwo.objects.all()
#     serializer_class = CategoryTwoModelSerializers
#
#
# class SubCategoryTwoModelViewSet(mixins.RetrieveModelMixin,
#                                  mixins.ListModelMixin,
#                                  GenericViewSet):
#     permission_classes = (AllowAny,)
#     queryset = SubCategoryTwo.objects.all()
#     serializer_class = SubCategoryTwoModelSerializers
#
#
# class SubCategoryTwoFileModelViewSet(mixins.RetrieveModelMixin,
#                                      mixins.ListModelMixin,
#                                      GenericViewSet):
#     permission_classes = (AllowAny,)
#     queryset = SubCategoryTwoFile.objects.all()
#     serializer_class = SubCategoryTwoFileModelSerializers
#
#
class CombinedTitleListAPIView(generics.ListAPIView):
    serializer_class = CombinedTitleSerializer

    def get_queryset(self):
        total_doc_titles = TotalDoc.objects.all().values('id', 'title')
        category_one_titles = CategoryOne.objects.all().values('id', 'title')
        category_two_titles = CategoryTwo.objects.all().values('id', 'title')

        combined_titles = [{'id': item['id'], 'title': item['title'], 'source': 'TotalDoc'} for item in
                           total_doc_titles]
        combined_titles += [{'id': item['id'], 'title': item['title'], 'source': 'CategoryOne'} for item in
                            category_one_titles]
        combined_titles += [{'id': item['id'], 'title': item['title'], 'source': 'CategoryTwo'} for item in
                            category_two_titles]

        return combined_titles

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

#     # lookup_field = 'category'
#
#     @swagger_auto_schema(tags=['Extract titles by category_id: url?category_id=id'])
#     @action(detail=False, methods=['GET'])
#     def category_titles(self, request):
#         category_id = request.query_params.get('category_id')
#         if category_id:
#             try:
#                 category = Category.objects.get(id=category_id)
#                 titles = CategoryTitle.objects.filter(category=category)
#
#                 student = request.user.id
#                 serializer = self.get_serializer(titles, many=True)
#
#                 k = 0
#                 title_mark = CategoryTitle.objects.filter(category=category_id)
#                 # TitleFile.objects.filter(title_id=title_id, status=True)
#                 for n in title_mark:
#                     title = CategoryTitle.objects.filter(title=n.title).first()
#                     # print(title)
#                     # n.title.id= title_mark.
#                     if n.mark and TitleFile.objects.filter(title=title, student=student, status=True):
#                         k += n.mark
#                     category.marks = k
#
#                     with transaction.atomic():
#                         category.save()
#
#                 print('title mark: ', k)
#
#                 # category = CategoryTitle.objects.get(category=category_id)
#                 # for n in category.mark:
#                 #     print(n)
#
#                 return Response(serializer.data)
#             except Category.DoesNotExist:
#                 return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
#         else:
#             return Response({'error': 'Category ID is required'}, status=status.HTTP_400_BAD_REQUEST)
#
#
# class TitleFileModelViewSet(mixins.CreateModelMixin,
#                             mixins.RetrieveModelMixin,
#                             mixins.UpdateModelMixin,
#                             mixins.DestroyModelMixin,
#                             mixins.ListModelMixin,
#                             GenericViewSet):
#     permission_classes = (IsAuthenticated,)
#     queryset = TitleFile.objects.all()
#     serializer_class = TitleFileModelSerializers
#     # pagination_class = LimitOffsetPagination
#     parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)
#
#     # def get_permissions(self):
#     #     if self.request.method == 'GET':
#     #         return [IsAuthenticated()]
#     #     if self.request.method == 'PATCH':
#     #         return [IsAdmin()]
#     #     else:
#     #         return super().get_permissions()
#
#     @swagger_auto_schema(operation_description='Upload file...', )
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         file = serializer.validated_data.get('file')
#         title = serializer.validated_data.get('title')
#         if not title:
#             return Response({'error': 'No title!'}, status=status.HTTP_400_BAD_REQUEST)
#         if not file:
#             return Response({'error': 'File upload error!'}, status=status.HTTP_400_BAD_REQUEST)
#
#         serializer.save()
#         return Response({'success': 'Create success!'}, status=status.HTTP_200_OK)
#
#     @swagger_auto_schema(tags=['Extract files by title_id: url?title_id=id'])
#     @action(detail=False, methods=['GET'])
#     def title_files(self, request):
#         title_id = request.query_params.get('title_id')
#         if title_id:
#             try:
#                 title = CategoryTitle.objects.get(id=title_id)
#                 files = TitleFile.objects.filter(title=title)
#                 serializer = self.get_serializer(files, many=True)
#
#                 student = TitleFile.objects.filter(student_id=3).first()
#                 true_count = TitleFile.objects.filter(title_id=title_id, student=int(student), status=True).count()
#                 print('status: ', true_count)
#                 title = CategoryTitle.objects.get(id=title_id)
#                 if not title.mark:
#                     if 1 <= true_count < 3:
#                         true_count = 3
#                     elif 3 <= true_count <= 4:
#                         true_count = 5
#                     elif 5 <= true_count:
#                         true_count = 8
#                     title.mark = true_count
#                     with transaction.atomic():
#                         title.save()
#
#                 # category = CategoryTitle.objects.get(category=category_id)
#
#                 return Response(serializer.data)
#             except CategoryTitle.DoesNotExist:
#                 return Response({'error': 'Title not found'}, status=status.HTTP_404_NOT_FOUND)
#         else:
#             return Response({'error': 'Title ID is required'}, status=status.HTTP_400_BAD_REQUEST)

# class AdminTitleFileUpdateModelView(
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.ListModelMixin,
#                    GenericViewSet):
#     permission_classes = (IsAuthenticated,)
#     queryset = TitleFile.objects.all()
#     serializer_class = AdminTitleFileModelSerializers
#     http_method_names = ['get', 'patch']
#
#     def get_permissions(self):
#         if self.request.method == 'GET':
#             return [IsAdmin()]
#         else:
#             return super().get_permissions()
#
#     @swagger_auto_schema(tags=['Admin'])
#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)
#
#     def perform_update(self, serializer):
#         serializer.save()
#
#     @swagger_auto_schema(tags=['Change the status of the admin file'])
#     def partial_update(self, request, *args, **kwargs):
#         kwargs['partial'] = True
#         return self.update(request, *args, **kwargs)



# def handling_404(request, exception):
#     return render(request, '404.html', {})
#
#
# def handling_500(request):
#     return render(request, '500.html')
