from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', views.home, name='home'),
    url(r'^post/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^post/drafts/$', views.post_draft_list, name='post_draft_list'),
	url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
	url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
	url(r'^post/comment/(?P<pk>\d+)/remove/$', views.post_comment_remove, name='post_comment_remove'),
	url(r'^accounts/signup/$', views.signup, name='signup'),
	url(r'^profile/edit/$', views.update_profile, name="profile_edit"),
	url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name="profile_view"),
	url(r'^contact/$', views.contact, name="contact"),
	url(r'^enquiry/(?P<pk>\d+)/remove/$', views.contact_remove, name='contact_remove'),
	url(r'^development/tools/$', views.dev_tools, name='dev_tools'),
	url(r'^like/(?P<pk>\d+)/$', views.like, name='like'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)