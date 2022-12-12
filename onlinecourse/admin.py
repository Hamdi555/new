from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question,Choice,Submission

# <HINT> Register QuestionInline and ChoiceInline classes here
# class QuestionInline(admin.StackedInline):
#     model = Question
#     min_num = 1
#     max_num = 10
    
class ChoiceInline(admin.TabularInline):
    model = Choice
    min_num = 1
    max_num = 5
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

class QuestionAdmin(admin.ModelAdmin):
    model= Question
    # list_display = ['question_text','grade']
    inlines = [ChoiceInline]
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice_text']
    
# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
