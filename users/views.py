from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from users.models import StudentUser, TeacherUser
from .serializers import StudentUserSerializer, TeacherUserSerializer, LoginSerializer, StudentUserListSerializer, \
    TeacherUserListSerializer, StudentSerializer
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token


class StudentUserRegisterView(generics.CreateAPIView):
    queryset = StudentUser.objects.all()
    serializer_class = StudentUserSerializer


class StudentUserListRegisterView(generics.ListAPIView):
    queryset = StudentUser.objects.all()
    serializer_class = StudentUserListSerializer


class StudentUserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentUser.objects.all()
    serializer_class = StudentSerializer
    http_method_names = ['get', 'patch', 'delete']


class TeacherUserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeacherUser.objects.all()
    serializer_class = TeacherUserSerializer
    http_method_names = ['get', 'patch', 'delete']


class TeacherUserRegisterView(generics.CreateAPIView):
    queryset = TeacherUser.objects.all()
    serializer_class = TeacherUserSerializer


class TeacherUserListRegisterView(generics.ListAPIView):
    queryset = TeacherUser.objects.all()
    serializer_class = TeacherUserListSerializer


# class LoginView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = LoginSerializer(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return Response({'detail': 'Siz tizimga kirdingiz.'}, status=status.HTTP_200_OK)

class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            # Tokenni olish va o'chirish
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"detail": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)

#
# class AdminRegisterApiView(viewsets.GenericViewSet):
#     queryset = CustomUser.objects.all()
#     permission_classes = (permissions.IsAdminUser,)
#     serializer_class = RegisterSerializer
#
#     def create(self, request, *args, **kwargs):
#         try:
#             serializer = self.get_serializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#
#             user = serializer.instance
#             my_group, created = Group.objects.get_or_create(name='ADMIN')
#             my_group.user_set.add(user)
#
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
#
#
# class StudentRegisterApiView(viewsets.GenericViewSet):
#     queryset = StudentUser.objects.all()
#     permission_classes = (permissions.IsAuthenticated,)
#     serializer_class = StudentSerializer
#
#     def create(self, request, *args, **kwargs):
#         try:
#             serializer = self.get_serializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#
#             # Guruhga qo'shish
#             user = serializer.instance  # Sizning serializerdagi foydalanuvchi obyektingiz
#             my_owner_group, created = Group.objects.get_or_create(name='STUDENT')
#             my_owner_group.user_set.add(user)
#
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
#
#
# class UsersListApiView(generics.ListAPIView):
#     queryset = CustomUser.objects.all()
#     permission_classes = (permissions.IsAuthenticated,)
#     serializer_class = RegisterSerializer
#
#
# class UserDetailApiView(generics.RetrieveUpdateDestroyAPIView, generics.GenericAPIView):
#     permission_classes = (permissions.IsAdminUser,)
#     serializer_class = RegisterSerializer
#     queryset = CustomUser.objects.all()
#
#     def get_object(self):
#         user_id = self.kwargs.get('pk')
#         return get_object_or_404(CustomUser, pk=user_id)
#
#     # def get(self, request, *args, **kwargs):
#     #     return self.list(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class StudentDetailApiView(generics.RetrieveUpdateDestroyAPIView, generics.GenericAPIView):
#     permission_classes = (permissions.IsAdminUser,)
#     serializer_class = StudentSerializer
#     queryset = StudentUser.objects.all()
#
#     def get_object(self):
#         user_id = self.kwargs.get('pk')
#         return get_object_or_404(CustomUser, pk=user_id)
#
#     @swagger_auto_schema(tags=['student retrieve'])
#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)
#
#     @swagger_auto_schema(tags=['Student delete'])
#     def delete(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class StudentsListApiView(generics.ListAPIView):
#     queryset = StudentUser.objects.all()
#     permission_classes = (permissions.IsAuthenticated,)
#     serializer_class = StudentSerializer
#
#
# # class LoginApiView(generics.CreateAPIView):
# #     serializer_class = LoginSerializer
# #     permission_classes = (permissions.AllowAny,)
# #
# #     def create(self, request, *args, **kwargs):
# #         try:
# #             serializer = self.get_serializer(data=request.data)
# #             serializer.is_valid(raise_exception=True)
# #
# #             username = serializer.validated_data.get('username')
# #             password = serializer.validated_data.get('password')
# #
# #             user = authenticate(username=username, password=password)
# #
# #             if user is None:
# #                 return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
# #
# #             refresh = RefreshToken.for_user(user)
# #             refresh_ = str(refresh)
# #             access = str(refresh.access_token)
# #
# #             return Response({'refresh': refresh_, 'access': access}, status=status.HTTP_200_OK)
# #         except Exception as e:
# #             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
# #
# #
# class LogoutApiView(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def post(self, request):
#         try:
#             refresh_token = request.data["refresh_token"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#
#             return Response(status=status.HTTP_205_RESET_CONTENT)
#         except Exception as e:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
