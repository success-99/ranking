from rest_framework import serializers
from .models import StudentUser, TeacherUser
from rest_framework.exceptions import ValidationError

from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class StudentUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = StudentUser
        fields = ['user', 'group', 'birth_date', 'total_marks']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid(raise_exception=True):
            user = user_serializer.save()
        student_user = StudentUser.objects.create(user=user, **validated_data)
        return student_user


class TeacherUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = TeacherUser
        fields = ['user', 'position']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid(raise_exception=True):
            user = user_serializer.save()
        teacher_user = TeacherUser.objects.create(user=user, **validated_data)
        return teacher_user

# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, required=True)
#     password2 = serializers.CharField(write_only=True, required=True)
#
#     class Meta:
#         model = CustomUser
#         fields = ('id', 'username', 'password', 'password2', 'email')
#         extra_kwargs = {
#             'username': {'required': True},
#         }
#
#     def validate(self, attrs):
#         if attrs['username'].isdigit() or len(attrs['username']) < 4:
#             raise serializers.ValidationError({"username": "Username should not be numbers and should have at least 4 "
#                                                            "characters."})
#         if attrs['password'] != attrs['password2'] or len(attrs['password']) < 4:
#             raise serializers.ValidationError({"password": "Password fields didn't match or should have at least 4."})
#         return attrs
#
#     def create(self, validated_data):
#         username = validated_data['username'].lower()  # username ni lower() ga o'tkazish
#         user = CustomUser.objects.create_user(
#             username=username,
#             password=validated_data['password'],
#             email=validated_data.get('email', ''),
#         )
#
#         user.set_password(validated_data['password'])
#         user.save()
#
#         return user

#


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'), username=username, password=password)
            if user is None:
                raise serializers.ValidationError(_("Unable to log in with provided credentials."), code='authorization')
        else:
            raise serializers.ValidationError(_("Must include 'username' and 'password'."), code='authorization')

        data['user'] = user
        return data


# class LoginStudentSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)
#
#     def validate(self, data):
#         username = data.get('username')
#         password = data.get('password')
#
#         if username and password:
#             user = StudentUser.objects.filter(username=username).first()
#             if not user:
#                 msg = 'Username invalid!'
#                 raise ValidationError(msg, code='authorization')
#             if not user.check_password(password):
#                 msg = 'Parol invalid!'
#                 raise ValidationError(msg, code='authorization')
#         else:
#             msg = 'Foydalanuvchi nomi va parolni kiriting'
#             raise ValidationError(msg, code='authorization')
#
#         return data

#
# class StudentSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, required=True)
#     password2 = serializers.CharField(write_only=True, required=True)
#
#     class Meta:
#         model = StudentUser
#         fields = (
#             'id', 'username', 'password', 'password2', 'first_name', 'last_name', 'gpa', 'birth_date')
#
#     def validate(self, attrs):
#         if attrs['username'].isdigit() or len(attrs['username']) < 4:
#             raise serializers.ValidationError({"username": "Username should not be numbers and should have at least 4 "
#                                                            "characters."})
#         if attrs['password'] != attrs['password2'] or len(attrs['password']) < 4:
#             raise serializers.ValidationError({"password": "Password fields didn't match or should have at least 4."})
#         return attrs
#
#     def create(self, validated_data):
#         username = validated_data['username'].lower()  # username ni lower() ga o'tkazish
#         user = StudentUser.objects.create_user(
#             username=username,
#             password=validated_data['password'],
#             first_name=validated_data.get('first_name', ''),
#             last_name=validated_data.get('last_name', ''),
#             birth_date=validated_data.get('birth_date', ''),
#             gpa=validated_data.get('gpa', '')
#         )
#
#         user.set_password(validated_data['password'])
#         user.save()
#
#         return user
