from django.conf.urls import include, url
from django.contrib import admin
from beeApp import views

urlpattens = [
	url(r'^add/(?P<comment_text>[\w]+)/(?P<comment_author>[\w]+)/(?P<comment_post>[\w]+)/(?P<comment_date_hour>[0-3][0-9]\\[0-1][0-9]\\[0-2][0-9][0-9][0-9]\:[0-2][0-9]\:[0-5][0-9])', views.add_comment),
	url(r'^delete/(?P<para_comment_id>[0-9]+)', views.delete_comment),
	url(r'^like_comment/(?P<para_comment_id>)[0-9]+/(?P<comment_person_id>[\w]+)', views.like_comment),
	url(r'^get_comment_likes/(?P<para_comment_id>[0-9]+)', views.get_comment_likes),
	url(r'^report_comment/(?P<para_comment_id>[0-9]+)/(?P<comment_person_id>[\w]+)', views.report_comment),
	url(r'^get_comment_report/(?P<para_comment_id>[0-9]+)', views.get_comment_report),
	url(r'^update_comment_text/(?P<para_comment_id>[0-9]+)/(?P<comment_text>[\w]+)', views.update_comment_text),
	url(r'^$', views.get_all)
]