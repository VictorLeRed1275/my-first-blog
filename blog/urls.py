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
	url(r'^shop/$', views.item_list, name='item_list'),
    url(r'^shop/(?P<pk>\d+)/$', views.item_detail, name='item_detail'),
	url(r'^shop/new/$', views.item_new, name='item_new'),
	url(r'^shop/(?P<pk>\d+)/edit/$', views.item_edit, name='item_edit'),
	url(r'^shop/drafts/$', views.item_draft_list, name='item_draft_list'),
	url(r'^shop/(?P<pk>\d+)/publish/$', views.item_publish, name='item_publish'),
	url(r'^shop/(?P<pk>\d+)/remove/$', views.item_remove, name='item_remove'),
	url(r'^post/comment/(?P<pk>\d+)/remove/$', views.post_comment_remove, name='post_comment_remove'),
	url(r'^shop/review/(?P<pk>\d+)/remove/$', views.item_review_remove, name='item_review_remove'),
	url(r'^accounts/signup/$', views.signup, name='signup'),
	url(r'^profile/edit/$', views.update_profile, name="profile_edit"),
	url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name="profile_view"),
	url(r'^contact/$', views.contact, name="contact"),
	url(r'^contact/list/$', views.contact_list, name="contact_list"),
	url(r'^enquiry/(?P<pk>\d+)/remove/$', views.contact_remove, name='contact_remove'),
	url(r'^development/tools/$', views.dev_tools, name='dev_tools'),
	url(r'^cart/remove/(?P<pk>\d+)/$', views.cart_remove, name='cart_remove'),
	url(r'^cart/add/(?P<pk>\d+)/$', views.cart_add, name='cart_add'),
	url(r'^cart/(?P<pk>\d+)/$', views.cart, name='cart'),
	
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)