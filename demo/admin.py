from django.contrib import admin
class prouduct_Admin(admin.ModelAdmin):
    # list_display=[]
    list_filter=['size']
    search_fields=['name']
    list_display=['name',"price","size","Is_huge"]
# Register your models here.
from .models import  comment, courses, item, product, student
admin.site.register(student)
admin.site.register(courses)
admin.site.register(comment)
admin.site.register(product,prouduct_Admin)