from django.contrib import admin


from .models import TotalDoc, CategoryOne, CategoryTwo, SubCategoryTwo, SubCategoryTwoFile, TotalDocUser, SubCategoryTwoUser,CategoryOneUser,CategoryTwoUser

admin.site.register(TotalDoc)
admin.site.register(CategoryOne)
admin.site.register(CategoryTwo)
admin.site.register(SubCategoryTwo)
admin.site.register(SubCategoryTwoFile)
admin.site.register(TotalDocUser)
admin.site.register(CategoryOneUser)
admin.site.register(CategoryTwoUser)
admin.site.register(SubCategoryTwoUser)