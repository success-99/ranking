from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.core.exceptions import ValidationError


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser, BaseModel):
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), blank=True)


class StudentUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group = models.CharField(_("group"), max_length=150)
    birth_date = models.DateField(null=True, blank=True)
    total_marks = models.PositiveIntegerField(_("Total Marks"), default=0)

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = _("Student User")
        verbose_name_plural = _("Student Users")

    def clean(self):
        if TeacherUser.objects.filter(user=self.user).exists():
            raise ValidationError(_('User cannot be both a student and a teacher.'))

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class TeacherUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    position = models.CharField(_("position"), max_length=150, blank=True)

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = _("Teacher User")
        verbose_name_plural = _("Teacher Users")

    def clean(self):
        if StudentUser.objects.filter(user=self.user).exists():
            raise ValidationError(_('User cannot be both a teacher and a student.'))

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

