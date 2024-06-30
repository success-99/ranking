from django.db import models
from users.models import StudentUser, BaseModel
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator


class TotalDoc(BaseModel):
    title = models.CharField(_("total doc title"), unique=True, max_length=255)
    mark = models.PositiveIntegerField(_("total doc mark"), default=0, validators=[MinValueValidator(0),
                                                                                   MaxValueValidator(5)])

    def __str__(self):
        return self.title


class TotalDocUser(BaseModel):
    student = models.ForeignKey(StudentUser, related_name="total_doc_user", on_delete=models.SET_NULL, null=True,
                                blank=True)
    title = models.ForeignKey(
        TotalDoc,
        on_delete=models.CASCADE,
        related_name="total_doc_users",
        related_query_name="total_doc_user",
    )

    def __str__(self):
        return f"{self.title}: {self.student}"


class CategoryOne(BaseModel):
    title = models.CharField(_("category_one title"), unique=True, max_length=255)
    file = models.FileField(_("category_one file"), null=True, blank=True)
    mark = models.PositiveIntegerField(_("category_one mark"), default=0, validators=[MinValueValidator(0),
                                                                                      MaxValueValidator(20)])

    def __str__(self):
        return self.title


class CategoryOneUser(BaseModel):
    student = models.ForeignKey(StudentUser, related_name="category_one_user", on_delete=models.SET_NULL, null=True,
                                blank=True)
    title = models.ForeignKey(
        CategoryOne,
        on_delete=models.CASCADE,
        related_name="category_one_users",
        related_query_name="category_one_user",
    )

    def __str__(self):
        return f"{self.title}: {self.student}"


class CategoryTwo(BaseModel):
    title = models.CharField(_("category_two title"), unique=True, max_length=255)
    marks = models.PositiveIntegerField(_("category_two mark"), default=0, validators=[MinValueValidator(0),
                                                                                       MaxValueValidator(20)])

    def __str__(self):
        return self.title


class CategoryTwoUser(BaseModel):
    student = models.ForeignKey(StudentUser, related_name="category_two_user", on_delete=models.SET_NULL, null=True,
                                blank=True)
    title = models.ForeignKey(
        CategoryTwo,
        on_delete=models.CASCADE,
        related_name="category_two_users",
        related_query_name="category_two_user",
    )

    def __str__(self):
        return f"{self.title}: {self.student}"


class SubCategoryTwo(BaseModel):
    title = models.ForeignKey(
        CategoryTwo,
        on_delete=models.CASCADE,
        related_name="sub_category_two",
        related_query_name="sub_category_two",
    )
    sub_title = models.CharField(_("sub_category_two title"), unique=True, max_length=255)
    mark = models.PositiveIntegerField(_("sub_category_two mark"), default=0, validators=[MinValueValidator(0),
                                                                                          MaxValueValidator(8)])

    def __str__(self):
        return self.sub_title


class SubCategoryTwoUser(BaseModel):
    student = models.ForeignKey(StudentUser, related_name="sub_category_two_users", on_delete=models.SET_NULL,
                                null=True,
                                blank=True)
    title = models.ForeignKey(
        SubCategoryTwo,
        on_delete=models.CASCADE,
        related_name="sub_category_two_users",
        related_query_name="sub_category_two_user",
    )

    def __str__(self):
        return f"{self.title}: {self.student}"


class SubCategoryTwoFile(BaseModel):
    title = models.ForeignKey(
        SubCategoryTwo,
        on_delete=models.CASCADE,
        related_name="sub_category_two_files",
        related_query_name="sub_category_two_file",
    )
    student = models.ForeignKey(StudentUser, on_delete=models.CASCADE, related_name="sub_category_two_files")

    file = models.FileField(_("sub_category_two_file file"))
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)
