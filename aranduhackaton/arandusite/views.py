from django.shortcuts import render
from django.views.generic import base
from django.core.urlresolvers       import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators        import method_decorator
from django.views.generic           import TemplateView, DetailView
from django.views.generic.edit      import FormView, UpdateView
from django.views.generic.edit      import FormMixin
from arandusite.models              import UserProfile

import logging
from arandusite        import forms
from arandusite.models import Area
from arandusite.models import Course
from arandusite.models import LearningList
from arandusite.models import LearningVideo

class AreaListMixin(object):
  def areas(self):
    return Area.objects.all()

# Create your views here. 
class MainView(AreaListMixin, TemplateView):
  template_name='arandusite/main.html'

@method_decorator(login_required, name='dispatch')
class ProfileView(AreaListMixin, TemplateView):
  template_name='arandusite/profile.html'

@method_decorator(login_required, name='dispatch')
class BadgesView(AreaListMixin, TemplateView):
  template_name='arandusite/badges.html'

@method_decorator(login_required, name='dispatch')
class ProgressView(AreaListMixin,TemplateView):
  template_name='arandusite/progress.html'

@method_decorator(login_required, name='dispatch')
class GroupsView(AreaListMixin,TemplateView):
  template_name='arandusite/groups.html'

class MissionView(AreaListMixin,TemplateView):
  template_name='arandusite/mission.html'

class StaffView( AreaListMixin,TemplateView):
  template_name='arandusite/staff.html'

class AboutView( AreaListMixin,TemplateView):
  template_name='arandusite/about.html'

@method_decorator(login_required, name='dispatch')
class SettingsView(AreaListMixin,UpdateView):
  model      = UserProfile
  form_class = forms.SettingsForm
  template_name = 'arandusite/settings.html'
  success_url = '/'
  def get_object(self, queryset=None):
    return self.request.user.userprofile


@method_decorator(login_required, name='dispatch')
class AreaView(AreaListMixin, DetailView):
  model=Area
  template_name = 'arandusite/area.html'

@method_decorator(login_required, name='dispatch')
class CourseView(AreaListMixin,DetailView):
  model=Course
  template_name = 'arandusite/course.html'

  
@method_decorator(login_required, name='dispatch')
class LearningListView(AreaListMixin, FormMixin, DetailView):
  model=LearningList
  template_name = 'arandusite/learninglist.html'
  form_class    = forms.AnnotationsForm

@method_decorator(login_required, name='dispatch')
class VideoView(TemplateView):
  template_name = 'arandusite/video.html'
  def get_video(self):
    return LearningVideo.objects.get(
      learningitem__id = self.kwargs['video_id']
    )