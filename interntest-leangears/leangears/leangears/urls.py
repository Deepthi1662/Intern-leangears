
from django.conf.urls import url
from django.contrib import admin

from django.contrib.auth import views as auth_views
from blog.views import blog_home, post_create, post_delete, post_details, post_update

urlpatterns = [

   
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^post_create/$', post_create, name='post_create'),
    url(r'^post_details/(?P<pk>[0-9]+)/$', post_details, name='post_details'),
    url(r'^post_update/(?P<pk>[0-9]+)/$', post_update, name='post_update'),
    url(r'^post_delete/(?P<pk>[0-9]+)/$', post_delete, name='post_delete'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', blog_home, name='blog_home'),

]
