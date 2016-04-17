from django import forms
from arandusite.models import UserProfile
from django.utils.translation import ugettext_lazy as _
from django.db import models
from tinymce.models import HTMLField


class SettingsForm(forms.ModelForm):
  biography = forms.CharField(max_length=160, widget=forms.Textarea, label=_('biography'))
  class Meta:
    model         = UserProfile
    exclude = ('location','user')

class AnnotationsForm(forms.Form):
  annotation = HTMLField()