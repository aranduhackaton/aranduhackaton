from django.contrib import admin
from django.contrib.auth.admin  import UserAdmin as BaseUserAdmin
from arandusite.models          import UserProfile
from arandusite.models          import Area
from arandusite.models          import Course
from arandusite.models          import LearningList
from arandusite.models          import LearningItem
from arandusite.models          import LearningVideo
from arandusite.models          import Skill
from arandusite.models          import ProfessionalProfile
from django.contrib.auth.models import User

# Inlines
class UserProfileInline(admin.TabularInline):
  model = UserProfile
  can_delete = False
  verbose_name_plural = 'User Profiles'

class AreaCourseInline(admin.TabularInline):
  model = Course
  extra = 3

class CourseLearningListInline(admin.TabularInline):
  model = LearningList
  extra = 3
class LearningListVideoInline(admin.TabularInline):
  model = LearningVideo
  extra = 3

# Register your models here.
class UserAdmin(BaseUserAdmin):
  inlines = (UserProfileInline,)

class AreaAdmin(admin.ModelAdmin):
  inlines = [AreaCourseInline]
class CourseAdmin(admin.ModelAdmin):
  inlines = [CourseLearningListInline]
  list_filter = ['area']
class LearningListAdmin(admin.ModelAdmin):
  inlines = [LearningListVideoInline]
class LearningVideoAdmin(admin.ModelAdmin):
  inlines = []
class SkillAdmin(admin.ModelAdmin):
  inlines = []
class ProfessionalProfileAdmin(admin.ModelAdmin):
  inlines = []


admin.site.unregister(User)
admin.site.register(User  , UserAdmin)
admin.site.register(Area  , AreaAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(LearningList, LearningListAdmin)
admin.site.register(LearningVideo, LearningVideoAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(ProfessionalProfile, ProfessionalProfileAdmin)