import os

from django.db import models
from users.models import StudentUser, BaseModel
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_delete
from django.dispatch import receiver


class TotalDoc(BaseModel):
    title = models.CharField(_("total doc title"), unique=True, max_length=255)

    def __str__(self):
        return self.title


class TotalDocUser(BaseModel):
    student = models.ForeignKey(StudentUser, related_name="total_doc_student_users", on_delete=models.CASCADE,
                                null=True, blank=True)
    title = models.ForeignKey(
        TotalDoc,
        on_delete=models.CASCADE,
        related_name="total_doc_title_users",
        related_query_name="total_doc_title_user",
    )
    mark = models.PositiveIntegerField(_("total doc mark"), default=0, validators=[MinValueValidator(0),
                                                                                   MaxValueValidator(5)])

    def __str__(self):
        return f"{self.title}: {self.student}"


class CategoryOne(BaseModel):
    title = models.CharField(_("category_one title"), unique=True, max_length=255)

    def __str__(self):
        return self.title


class CategoryOneUser(BaseModel):
    student = models.OneToOneField(StudentUser, related_name="category_one_student_users", on_delete=models.CASCADE,
                                   null=True, blank=True)
    title = models.ForeignKey(
        CategoryOne,
        on_delete=models.CASCADE,
        related_name="category_one_title_users",
        related_query_name="category_one_title_user",
    )
    file = models.FileField(_("category_one file"), null=True, blank=True)
    mark = models.PositiveIntegerField(_("category_one mark"), default=0, validators=[MinValueValidator(0),
                                                                                      MaxValueValidator(20)])

    def __str__(self):
        return f"{self.title}: {self.student}"


@receiver(post_delete, sender=CategoryOneUser)
def delete_file(sender, instance, **kwargs):
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)


class CategoryTwo(BaseModel):
    title = models.CharField(_("category_two title"), unique=True, max_length=255)

    def __str__(self):
        return self.title


class CategoryTwoUser(BaseModel):
    student = models.OneToOneField(StudentUser, related_name="category_two_student_users", on_delete=models.CASCADE,
                                   null=True,
                                   blank=True)
    title = models.ForeignKey(
        CategoryTwo,
        on_delete=models.CASCADE,
        related_name="category_two_title_users",
        related_query_name="category_two_title_user",
    )
    mark = models.PositiveIntegerField(_("category_two mark"), default=0, validators=[MinValueValidator(0),
                                                                                      MaxValueValidator(20)])

    def __str__(self):
        return f"{self.title}: {self.student}"


class SubCategoryTwo(BaseModel):
    title = models.ForeignKey(
        CategoryTwo,
        on_delete=models.CASCADE,
        related_name="sub_category_title_twos",
        related_query_name="sub_category_title_two",
    )
    sub_title = models.CharField(_("sub_category_two title"), unique=True, max_length=255)

    def __str__(self):
        return self.sub_title


class SubCategoryTwoUser(BaseModel):
    student = models.OneToOneField(StudentUser, related_name="sub_category_two_student_users",
                                   on_delete=models.CASCADE,
                                   null=True,
                                   blank=True)
    sub_title = models.ForeignKey(
        SubCategoryTwo,
        on_delete=models.CASCADE,
        related_name="sub_category_two_sub_title_users",
        related_query_name="sub_category_two_sub_title_user",
    )

    mark = models.PositiveIntegerField(_("student mark"), default=0, validators=[MinValueValidator(0),
                                                                                 MaxValueValidator(8)])

    def __str__(self):
        return f"{self.sub_title}: {self.student}"

    def update_mark_based_on_approved_files(self):
        # Count the approved files for this student and subcategory
        approved_file_count = self.sub_title.sub_category_two_title_files.filter(is_approved=True,
                                                                                 student=self.student).count()
        # Update the mark field
        self.mark = approved_file_count
        self.save()


class SubCategoryTwoFile(BaseModel):
    sub_title = models.ForeignKey(
        SubCategoryTwo,
        on_delete=models.CASCADE,
        related_name="sub_category_two_title_files",
        related_query_name="sub_category_two_title_file",
    )
    student = models.ForeignKey(StudentUser, on_delete=models.CASCADE, related_name="sub_category_two_student_files")

    file = models.FileField(_("sub_category_two_file file"))
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update the mark for the related SubCategoryTwo instance
        self.sub_title.update_mark_based_on_approved_files()


@receiver(post_delete, sender=SubCategoryTwoFile)
def delete_file(sender, instance, **kwargs):
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)
