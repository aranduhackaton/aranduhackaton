from modeltranslation.translator import translator, TranslationOptions
from arandusite.models import Area
from arandusite.models import LearningList
from arandusite.models import Skill
from arandusite.models import Course
from arandusite.models import LearningVideo
from arandusite.models import ProfessionalProfile

class AreaTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
class CourseTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
class SkillTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
class LearningListTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
class LearningVideoTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
class ProfessionalProfileTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)



translator.register(Area        , AreaTranslationOptions)
translator.register(Course      , CourseTranslationOptions)
translator.register(Skill       , TranslationOptions)
translator.register(LearningList, LearningListTranslationOptions)
translator.register(LearningVideo, LearningVideoTranslationOptions)
translator.register(ProfessionalProfile, ProfessionalProfileTranslationOptions)