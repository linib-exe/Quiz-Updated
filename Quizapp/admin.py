from django.contrib import admin
from .models import Quiz,Question,Choice,Profile

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Profile)
# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'score')

