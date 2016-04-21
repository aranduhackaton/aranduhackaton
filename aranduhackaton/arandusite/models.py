from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
import datetime
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class ItemBase(models.Model):
  owner   = models.ForeignKey(User, related_name='%(class)s_related')
  title   = models.CharField(max_length=250)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

class Commentable(models.Model):
  user    = models.ForeignKey(User)
  comment = models.TextField()
  date    = models.DateField(default=datetime.date.today)
  class Meta:
    abstract = True


# Create your models here.
class UserProfile(models.Model):
  """
  Information about the user
  """
  GENDERS       = (('male', _('MALE')), ('female', _('FEMALE')))
  user          = models.OneToOneField(User, on_delete=models.CASCADE)
  birthday      = models.DateField(default=datetime.date.today)
  biography     = models.CharField(max_length=160, blank=True)
  gender        = models.CharField(max_length=16, choices=GENDERS, blank=True)
  picture       = models.ImageField(upload_to='profile_images', blank=True)
  website       = models.URLField(blank=True)
  def __str__(self):
    return "{0} {1}".format(self.user.first_name, self.user.last_name)

class Area(models.Model):
  """
  Major cluster of subjects (e.g. Computing, Mathematics, History...)
  """
  code          = models.CharField(max_length=255)
  title         = models.CharField(max_length=255)
  description   = models.TextField(blank=True)
  def __str__(self):
    return self.code

class Course(models.Model):
  """
  Second division (e.g. Computer Graphics, Calculus)
  A course has several lists (below)
  """
  code          = models.CharField(max_length=255)
  area          = models.ForeignKey(Area)
  title         = models.CharField(max_length=255)
  description   = models.TextField(blank=True)
  def __str__(self):
    return self.code

class LearningItem(models.Model):
  """
  A resource which appears at a list 
  """
  code          = models.CharField(max_length=64)
 
class LearningList(models.Model):
  """
  List of learning activities (videos, texts, exercises, demos, ...)
  """
  title         = models.CharField(max_length=255)
  description   = models.TextField(blank=True)
  course        = models.ForeignKey(Course)
  owner         = models.ForeignKey(User)
  #items         = models.OneToManyField( ManyToManyField(LearningItem, through='LearningListItem')
  code          = models.CharField(max_length=255)
  order         = models.IntegerField()
  thumbnail     = models.ImageField(upload_to='learning_list/thumbnail')
  def __str__(self):
    return self.code

class LearningListItem(models.Model):
  """
  Items of a list (list `many-to-many` item)
  """
  learning_item = models.ForeignKey(LearningItem, on_delete=models.CASCADE)
  learning_list = models.ForeignKey(LearningList, on_delete=models.CASCADE)
  item_order    = models.IntegerField()

class LearningVideo(models.Model):
  """
  Any video
  """
  learning_list = models.ForeignKey(LearningList, blank=True)
  url           = models.URLField()
  title         = models.CharField(max_length=255)
  description   = models.TextField(blank=True)
  def __str__(self):
    return self.title

class Skill(models.Model):
  """
  @brief  ""
  """
  title = models.CharField(max_length=255)
  description = models.TextField(blank=True)

class SkillsVideo(models.Model):
  """
  @brief      { class_description }
  """
  video = models.ForeignKey(LearningVideo)
  skill = models.ForeignKey(Skill)


class ProfessionalProfile(models.Model):
  skills      = models.ManyToManyField(Skill)
  title       = models.CharField(max_length=255)
  description = models.TextField(blank=True)

class UserVideo():
  """
  @brief      { class_description }
  """
  user  = models.ForeignKey(User)
  video = models.ForeignKey(LearningVideo)
  score = models.IntegerField()
