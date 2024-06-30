from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from rest_framework_simplejwt.views import TokenBlacklistView, TokenRefreshView, TokenObtainPairView

from .views import StudentUserRegisterView, TeacherUserRegisterView, LoginView
#
# router = DefaultRouter()
#
#
# router.register('register-admin', AdminRegisterApiView, basename='register-admin')
# router.register('register-student', StudentRegisterApiView, basename='register-student')
#
urlpatterns = [
    path('student-register/', StudentUserRegisterView.as_view(), name='student-register'),
    path('teacher-register/', TeacherUserRegisterView.as_view(), name='teacher-register'),
    path('user-login/', LoginView.as_view(), name='user-login'),

    # path('user-detail/<int:pk>/', UserDetailApiView.as_view(), name='user-detail'),
    #
    # path('students-list/', StudentsListApiView.as_view(), name='student-list'),
    # path('student-detail/<int:pk>/', StudentDetailApiView.as_view(), name='student-detail'),

    # path('login/', LoginApiView.as_view(), name='login'),
    # path('logout/', LogoutApiView.as_view(), name='logout'),
    # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('refresh-token/', TokenRefreshView.as_view(), name='refresh-token'),
    # path('logout/', TokenBlacklistView.as_view(), name='logout'),

    # path('', include(router.urls)),

]
