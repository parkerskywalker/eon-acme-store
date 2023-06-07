from django.contrib import admin

from .models import Category, OperationType


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(OperationType)
class OperationTypeAdmin(admin.ModelAdmin):
    pass