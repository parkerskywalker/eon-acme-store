from django.contrib import admin

from .models import Operation

# Register your models here.
@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    pass
