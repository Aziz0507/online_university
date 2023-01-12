from django.shortcuts import render
from django.views.generic.base import View
from django.db import connection


from .models import Categories_models, Techer_models, lesson_models, Moduls_models, thems_video_models

# Create your views here.
class Main_views(View):
	def get(self, requests):
		# models = Categories_models.objects.get(id = pk)
		models = Categories_models.objects.all
		return render(requests, 'index.html', {'cat':models})

class Corses_view(View):
	def get(self, requests, pk):
		models = lesson_models.objects.filter(categoriy_lesson_id = pk)
		return render(requests, 'corses.html', {'les':models})

class Thems_view(View):
	# def get(self, requests, pu):
	# 	models  = Moduls_models.objects.filter(lesson_type_id = pu)
	# 	# model   = thems_video_models.objects.all()
	# 	models2 = thems_video_models.objects.raw(f"SELECT m.moduls_l, v.Moduls_type FROM {models} m, thems_video_models v WHERE m.moduls_l = v.Moduls_type")
	# 	return render(requests, 'thems.html', {'them':models, 'vid':models2})
	def get(self, requests, pu):
		cursor = connection.cursor()
		cursor.execute("SELECT m.*, v.* FROM ilm_pages_Moduls_models m, ilm_pages_thems_video_models v WHERE m.id = v.Moduls_type_id AND m.lesson_type_id = 1")
		result = dictfetchall(cursor)
		return render(requests, 'thems.html', {'result':result})

		

def dictfetchall(cursor):
	desc = cursor.description
	return [
		dict(zip([col[0] for col in desc], row))
		for row in cursor.fetchall()
	]

def SQL_lesson_view(requests):
	cursor = connection.cursor()
	cursor.execute("SELECT m.*, v.* FROM ilm_pages_Moduls_models m, ilm_pages_thems_video_models v WHERE m.id = v.Moduls_type_id")
	result = dictfetchall(cursor)
	return render(requests, 'SQL_lesson_view.html', {'sql':result})

class Lesson_video_view(View):
	def get(self, requests, slug):
		cursor = connection.cursor()
		cursor.execute(f"SELECT v.*, m.moduls_l, m.id  FROM ilm_pages_thems_video_models v, ilm_pages_Moduls_models m WHERE v.Moduls_type_id = {slug} AND {slug} = m.id")
		result = dictfetchall(cursor)

		return render(requests, 'videos.html', {'video':result})


	