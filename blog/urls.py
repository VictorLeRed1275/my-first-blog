from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^post/search/$', views.post_search, name='post_search'),
	url(r'^video/search/$', views.video_search, name='video_search'),
    url(r'^post/$', views.post_list, name='post_list'),
	url(r'^video/$', views.video_list, name='video_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^video/(?P<pk>\d+)/$', views.video_detail, name='video_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^video/new/$', views.video_new, name='video_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^video/(?P<pk>\d+)/edit/$', views.video_edit, name='video_edit'),
	url(r'^post/drafts/$', views.post_draft_list, name='post_draft_list'),
	url(r'^video/drafts/$', views.video_draft_list, name='video_draft_list'),
	url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
	url(r'^video/(?P<pk>\d+)/publish/$', views.video_publish, name='video_publish'),
	url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
	url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
	url(r'^video/(?P<pk>\d+)/remove/$', views.video_remove, name='video_remove'),
	url(r'^video/(?P<pk>\d+)/comment/$', views.add_comment_to_video, name='add_comment_to_video'),
	url(r'^post/comment/(?P<pk>\d+)/approve/$', views.post_comment_approve, name='post_comment_approve'),
	url(r'^post/comment/(?P<pk>\d+)/remove/$', views.post_comment_remove, name='post_comment_remove'),
	url(r'^video/comment/(?P<pk>\d+)/approve/$', views.video_comment_approve, name='video_comment_approve'),
	url(r'^video/comment/(?P<pk>\d+)/remove/$', views.video_comment_remove, name='video_comment_remove'),
	url(r'^accounts/signup/$', views.signup, name='signup'),
]