from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),

    url(r'^/post_list_sort_c/$', views.post_list_sort_c, name='post_list_sort_c'),
    url(r'^/post_list_sort_c_operator/$', views.post_list_sort_c_operator, name='post_list_sort_c_operator'),
    url(r'^/post_list_sort_html/$', views.post_list_sort_html, name='post_list_sort_html'),

]