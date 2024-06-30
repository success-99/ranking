from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TotalDoc, TotalDocUser, CategoryOne, CategoryOneUser, \
    CategoryTwo, CategoryTwoUser, SubCategoryTwo, SubCategoryTwoUser
from users.models import StudentUser
from django.db import transaction


@receiver(post_save, sender=StudentUser)
def create_related_models(sender, instance, created, **kwargs):
    if created:
        transaction.on_commit(lambda: create_models(instance))


def create_models(instance):
    if CategoryTwo.objects.exists():
        category_twos = CategoryTwo.objects.all()
        for category_two in category_twos:
            CategoryTwoUser.objects.create(student=instance, title=category_two)
    if SubCategoryTwo.objects.exists():
        sub_category_twos = SubCategoryTwo.objects.all()
        for sub_category_two in sub_category_twos:
            SubCategoryTwoUser.objects.create(student=instance, title=sub_category_two)
    if TotalDoc.objects.exists():
        total_docs = TotalDoc.objects.all()
        for total_doc in total_docs:
            TotalDocUser.objects.create(student=instance, title=total_doc)
    if CategoryOne.objects.exists():
        category_ones = CategoryOne.objects.all()
        for category_one in category_ones:
            CategoryOneUser.objects.create(student=instance, title=category_one)


# # post_save signal uchun receiver
# @receiver(post_save, sender=StudentUser)
# def create_total_doc_user(sender, instance, created, **kwargs):
#     if created:
#         if TotalDoc.objects.exists():
#             total_docs = TotalDoc.objects.all()
#             for total_doc in total_docs:
#                 TotalDocUser.objects.create(student=instance, title=total_doc)
#
#         if CategoryOne.objects.exists():
#             category_ones = CategoryOne.objects.all()
#             for category_one in category_ones:
#                 CategoryOneUser.objects.create(student=instance, title=category_one)
#
#         if CategoryTwo.objects.exists():
#             category_twos = CategoryTwo.objects.all()
#             for category_two in category_twos:
#                 CategoryTwoUser.objects.create(student=instance, title=category_two)
#
#         if SubCategoryTwo.objects.exists():
#             sub_category_twos = SubCategoryTwo.objects.all()
#             for sub_category_two in sub_category_twos:
#                 SubCategoryTwoUser.objects.create(student=instance, title=sub_category_two)
