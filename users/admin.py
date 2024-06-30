from django.contrib import admin


from .models import StudentUser, TeacherUser, User

admin.site.register(User)
admin.site.register(StudentUser)
admin.site.register(TeacherUser)
