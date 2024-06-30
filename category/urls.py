from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenBlacklistView, TokenRefreshView, TokenObtainPairView

from .views import TotalDocViewSet, CategoryOneModelViewSet,\
    TotalDocTeacherViewSet, CategoryOneTeacherModelViewSet,\
    CategoryOneStudentModelViewSet, SubCategoryTwoFileStudentModelViewSet,\
    CategoryTwoModelViewSet, SubCategoryTwoModelViewSet, SubCategoryTwoFileModelViewSet

router = DefaultRouter()


router.register('total-doc', TotalDocViewSet, basename='total-doc')
router.register('category-one', CategoryOneModelViewSet, basename='category-one')
router.register('category-two', CategoryTwoModelViewSet, basename='category-two')
router.register('subcategory-two', SubCategoryTwoModelViewSet, basename='subcategory-two')
router.register('subcategory-two-file', SubCategoryTwoFileModelViewSet, basename='subcategory-two-file')

router.register('total-doc-teacher', TotalDocTeacherViewSet, basename='total-doc-teacher')
router.register('category-one-teacher', CategoryOneTeacherModelViewSet, basename='category-one-teacher')

router.register('category-one-student', CategoryOneStudentModelViewSet, basename='category-one-student')
router.register('subcategory-two-file-student', SubCategoryTwoFileStudentModelViewSet, basename='subcategory-two-file-student')
urlpatterns = [

    path('', include(router.urls)),

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
