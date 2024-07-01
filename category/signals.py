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



@receiver(post_save, sender=CategoryTwo)
def create_category_two_users(sender, instance, created, **kwargs):
    if created:
        transaction.on_commit(lambda: _create_related_users(instance, CategoryTwoUser))

@receiver(post_save, sender=SubCategoryTwo)
def create_sub_category_two_users(sender, instance, created, **kwargs):
    if created:
        transaction.on_commit(lambda: _create_related_users(instance, SubCategoryTwoUser))

@receiver(post_save, sender=TotalDoc)
def create_total_doc_users(sender, instance, created, **kwargs):
    if created:
        transaction.on_commit(lambda: _create_related_users(instance, TotalDocUser))

@receiver(post_save, sender=CategoryOne)
def create_category_one_users(sender, instance, created, **kwargs):
    if created:
        transaction.on_commit(lambda: _create_related_users(instance, CategoryOneUser))

def _create_related_users(instance, UserClass):
    students = StudentUser.objects.all()
    for student in students:
        UserClass.objects.create(student=student, title=instance)


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

#
# @receiver(post_save, sender=CategoryTwo)
# def create_category_two_users(sender, instance, created, **kwargs):
#     if created:
#         transaction.on_commit(lambda: create_category_two_users(instance))
#
# def create_category_two_users1(instance):
#     students = StudentUser.objects.all()
#     for student in students:
#         CategoryTwoUser.objects.create(student=student, title=instance)
#
# @receiver(post_save, sender=SubCategoryTwo)
# def create_sub_category_two_users(sender, instance, created, **kwargs):
#     if created:
#         transaction.on_commit(lambda: create_sub_category_two_users(instance))
#
# def create_sub_category_two_users2(instance):
#     students = StudentUser.objects.all()
#     for student in students:
#         SubCategoryTwoUser.objects.create(student=student, sub_title=instance)
#
# @receiver(post_save, sender=TotalDoc)
# def create_total_doc_users(sender, instance, created, **kwargs):
#     if created:
#         transaction.on_commit(lambda: create_total_doc_users(instance))
#
# def create_total_doc_users3(instance):
#     students = StudentUser.objects.all()
#     for student in students:
#         TotalDocUser.objects.create(student=student, title=instance)
#
# @receiver(post_save, sender=CategoryOne)
# def create_category_one_users(sender, instance, created, **kwargs):
#     if created:
#         transaction.on_commit(lambda: create_category_one_users(instance))
#
# def create_category_one_users4(instance):
#     students = StudentUser.objects.all()
#     for student in students:
#         CategoryOneUser.objects.create(student=student, title=instance)