from django.contrib import admin

# Register your models here.
from mem.models import Muse

@admin.register(Muse)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('muse', 'ctime')
