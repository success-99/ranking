# from django.contrib.auth.models import Group
# from users.models import StudentUser
# from rest_framework import permissions
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
#
#
# class DeleteAllDataView(APIView):
#     permission_classes = (permissions.IsAdminUser,)
#
#     def post(self, request, *args, **kwargs):
#         # Teacher.objects.all().delete()
#         # Student.objects.all().delete()
#         # Course.objects.all().delete()
#         Group.objects.all().delete()
#         StudentUser.objects.filter(is_staff=False).delete()
#         return Response({'message': 'Hamma ma\'lumotlar muvaffaqiyatli o\'chirildi'}, status=status.HTTP_204_NO_CONTENT)
