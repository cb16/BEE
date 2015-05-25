from django.shortcuts import render
from beeApp.models import Tag, Badge
import json
from django.core import serializers
from django.http import HttpResponse

format = 'json'

# Create your views here.

#TAG'S VIEW
def add_tag(request, tag_title):
	if not (Tag.objects.filter(title = tag_title)):
		tag = Tag(title = tag_title)
		tag.save()
		return HttpResponse(serializers.serialize(format, [tag]))
	else:
		return HttpResponse(serializers.serialize(format, []))

def delete_tag(request, tag_title):
	tag = (Tag.objects.filter(title = tag_title))
	if tag:
		tag.delete()
		return HttpResponse(serializers.serialize(format, [tag]))
	else:
		return HttpResponse(serializers.serialize(format, []))

def change_title_tag(request, tag_title, new_title):
	tag = (Tag.objects.filter(title = tag_title))
	if tag:
		tag.title = new_title
		tag.save()
		return HttpResponse(serializers.serialize(format, [tag]))
	else:
		return HttpResponse(serializers.serialize(format, []))

def get_tag(request, tag_title):
	data = serializers.serialize(format, (Tag.objects.filter(title = tag_title)))
	return HttpResponse(data)

def get_all(request):
	data = serializers.serialize(format, Tag.objects.all())
	return HttpResponse(data)


#BADGE'S VIEW

def add_badge(request, badge_name, badge_description, badge_icon):
	if not (Badge.objects.filter(name = badge_name, description = badge_description, icon = badge_icon)):
		badge = Badge(name = badge_name, description = badge_description, icon = badge_icon)
		badge.save()
		return HttpResponse(serializers.serialize(format, [badge]))
	else:
		return HttpResponse(serializers.serialize(format, []))

def delete_badge(request, badge_name):
	badge = (Badge.objects.filter(name = badge_name))
	if badge:
		badge.delete()
		return HttpResponse(serializers.serialize(format, [badge]))
	else:
		return HttpResponse(serializers.serialize(format, []))


def change_name_badge(request, badge_name, new_name):
	badge = Badge.objects.filter(name = badge_name)
	if badge:
		badge[0].name = new_name
		badge[0].save()
		return HttpResponse(serializers.serialize(format, badge))
	else:
		return HttpResponse(serializers.serialize(format, []))

def change_description_badge(request, badge_name, new_description):
	badge = Badge.objects.filter(name = badge_name)
	if badge:
		badge[0].description = new_description
		badge[0].save()
		return HttpResponse(serializers.serialize(format, badge))
	else:
		return HttpResponse(serializers.serialize(format, []))

def change_icon_badge(request, badge_name, new_icon):
	badge = Badge.objects.filter(name = badge_name)
	if badge:
		badge[0].icon = new_icon
		badge[0].save()
		return HttpResponse(serializers.serialize(format, badge))
	else:
		return HttpResponse(serializers.serialize(format, []))

def get_badge_icon(request, badge_name):
	badge = Badge.objects.filter(name = badge_name)
	if badge:
		icon = badge[0].icon
		return HttpResponse(icon)
	else:
		return HttpResponse(serializers.serialize(format, []))

# COMMENTS VIEWS

def add_comment(request, comment_text, comment_author, comment_post, comment_date_hour):
	if not (Comment.objects.filter(text = comment_text, author = comment_autor, post = comment_post, date_hour = comment_date_hour)):
		comment = Comment(text = comment_text, author = comment_autor, post = comment_post, date_hour = comment_date_hour)
		comment.save()
		return HttpResponse(serializers.serialize(format, [comment]))
	else:
		return HttpResponse(serializers.serialize(format, []))

def delete_comment(request, para_comment_id):
	comment = Comment.objects.get(para_comment_id)
	if comment:
		comment.delete()
		return HttpResponse(serializers.serialize(format, [comment]))
	else:
		return HttpResponse(serializers.serialize(format, []))

def like_comment(request, para_comment_id, comment_person_id):
	like = Comment.comment_likes.objects.get(para_comment_id, comment_person_id)
	if like:
		like.delete()
		return HttpResponse(serializers.serialize(format, [like]))
	else:
		Comment.objects.get(para_comment_id).comment_likes.add(para_comment_id, comment_person_id)
		return HttpResponse(serializers.serialize(format, []))

def get_comment_likes(request, para_comment_id):
	likes = Comment.comment_likes.objects.filter(comment_id = para_comment_id).count()
	return HttpResponse(likes)

def report_comment(request, para_comment_id, comment_person_id):
	report = Comment.comment_reports.objects.get(para_comment_id, comment_person_id)
	if report:
		report.delete()
		return HttpResponse(serializers.serialize(format, [report]))
	else:
		Comment.objects.get(para_comment_id).comment_reports.add(para_comment_id, comment_person_id)
		return HttpResponse(serializers.serialize(format, []))

def get_comment_reports(request, para_comment_id):
	reports = Comment.comment_reports.objects.filter(comment_id = para_comment_id).count()
	return HttpResponse(reports)

def update_comment_text(request, para_comment_id, comment_text):
	comment = Comment.objects.get(para_comment_id)
	if comment:
		comment[0].text = comment_text
		comment[0].save()
		return HttpResponse(serializers.serialize(format, [comment]))
	else:
		return HttpResponse(serializers.serialize(format, []))

def get_all(request):
	data = serializers.serialize(format, Badge.objects.all())
	return HttpResponse(data)















