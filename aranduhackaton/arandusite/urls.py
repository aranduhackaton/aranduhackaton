from django.conf.urls import url, include
from django.contrib import admin
from arandusite import views

urlpatterns = [
  url(r'^accounts/', include('registration.backends.hmac.urls')),
  url(r'^settings',  views.SettingsView.as_view(), name='settings'),
  
  # Main page
  url(r'^$',         views.MainView.as_view(),     name='main'),
  url(r'^profile',   views.ProfileView.as_view(),  name='profile'),
  url(r'^badges',    views.BadgesView.as_view(),   name='badges'),
  url(r'^progress',  views.ProgressView.as_view(), name='progress'),
  url(r'^groups',    views.GroupsView.as_view(),   name='groups'),
  
  # For learning
  url(r'^learn/(?P<area_id>[0-9]+)/(?P<course_id>[0-9]+)/new'           , views.VideoNewView.as_view(), name='video-new'),
  url(r'^learn/(?P<area_id>[0-9]+)/(?P<course_id>[0-9]+)/(?P<pk>[0-9]+)', views.LearningListView.as_view(), name='list'),
  url(r'^learn/(?P<area_id>[0-9]+)/(?P<pk>[0-9]+)', views.CourseView.as_view(),       name='course'),
  url(r'^learn/(?P<pk>[0-9]+)', views.AreaView.as_view(), name='area'),
  
  #url(r'^course/(?P<course_id>[0-9]+)',                    views.CourseView.as_view(),       name='portal-course'),
  #url(r'^list/(?P<list_id>[0-9]+)/(?P<video_id>[0-9]+)',   views.VideoView.as_view(),        name='portal-video'),
  #url(r'^list/(?P<list_id>[0-9]+)',                        views.LearningListView.as_view(), name='portal-learninglist'),
  #url(r'^tinymce/', include('tinymce.urls')),

  # Other information
  url(r'^mission',   views.MissionView.as_view(),  name='mission'),
  url(r'^staff',     views.StaffView.as_view(),    name='staff'),
  url(r'^about',     views.AboutView.as_view(),    name='about'),

]