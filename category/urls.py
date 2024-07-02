from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenBlacklistView, TokenRefreshView, TokenObtainPairView

from .views import TotalDocRetrieveListModelMixinView, TotalDocUserRetrieveListModelMixinView,\
    TotalDocTeacherMarkUpdateModelMixinView, CategoryOneRetrieveListModelMixinView, \
    CategoryOneUserRetrieveListModelMixinView, CategoryOneStudentFileUpdateModelMixinView,\
    CategoryOneTeacherUpdateMarkModelMixinView, CombinedTitleListAPIView, CategoryTwoRetrieveListModelMixinView,\
    CategoryTwoUserRetrieveListModelMixinView, SubCategoryTwoRetrieveListModelMixinView


router = DefaultRouter()


router.register('total-doc-list', TotalDocRetrieveListModelMixinView, basename='total_doc_list')
router.register('total-doc-student-list', TotalDocUserRetrieveListModelMixinView, basename='total_doc_student_list')
router.register('total-doc-student-mark-update', TotalDocTeacherMarkUpdateModelMixinView, basename='total_doc_student_mark_update')

router.register('category-one-list', CategoryOneRetrieveListModelMixinView, basename='category_one_list')
router.register('category-one-student-list', CategoryOneUserRetrieveListModelMixinView, basename='category_one_student_file_list')
router.register('category-one-student-file-create', CategoryOneStudentFileUpdateModelMixinView, basename='category_one_student_file_create')
router.register('category-one-student-mark-create', CategoryOneTeacherUpdateMarkModelMixinView, basename='category_one_student_mark_create')

router.register('category-two-list', CategoryTwoRetrieveListModelMixinView, basename='category_two_list')
router.register('category-two-student-list', CategoryTwoUserRetrieveListModelMixinView, basename='category_one_student_list')

router.register('subcategory-two-list', SubCategoryTwoRetrieveListModelMixinView, basename='subcategory_two_list')



# router.register('subcategory-two-file', SubCategoryTwoFileModelViewSet, basename='subcategory_two_file')
#
#
# router.register('total-doc-teacher', TotalDocTeacherViewSet, basename='total_doc_teacher')
# router.register('category-one-teacher', CategoryOneTeacherModelViewSet, basename='category_one_teacher')
#
# router.register('category-one-student', CategoryOneStudentModelViewSet, basename='category_one_student')
# router.register('subcategory-two-file-student', SubCategoryTwoFileStudentModelViewSet, basename='subcategory_two_file'
#                                                                                                 '_student')
urlpatterns = [

    path('', include(router.urls)),
    path('all-category-title/', CombinedTitleListAPIView.as_view(), name='all_category_title'),

    #     path('user-list/', UsersListApiView.as_view(), name='list'),
    #     path('user-detail/<int:pk>/', UserDetailApiView.as_view(), name='user-detail'),
    #
    #     path('students-list/', StudentsListApiView.as_view(), name='student-list'),
    #     path('student-detail/<int:pk>/', StudentDetailApiView.as_view(), name='student-detail'),
    #
    #     # path('login/', LoginApiView.as_view(), name='login'),
    #     # path('logout/', LogoutApiView.as_view(), name='logout'),
    #     path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #     path('refresh-token/', TokenRefreshView.as_view(), name='refresh-token'),
    #     path('logout/', TokenBlacklistView.as_view(), name='logout'),

]
