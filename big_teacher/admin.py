from django.contrib import admin

# Register your models here.
from .models import Question

from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    fields = ['answer_text', 'question_text']

admin.site.register(Question)