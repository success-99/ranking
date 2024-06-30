from rest_framework.permissions import BasePermission
from .models import TeacherUser, StudentUser


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return StudentUser.objects.filter(user=request.user).exists()
        return False


class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return TeacherUser.objects.filter(user=request.user).exists()
        return False


class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return True
            else:
                return False
        else:
            return False
