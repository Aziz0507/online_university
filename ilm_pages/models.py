from django.db import models
from embed_video.fields import EmbedVideoField



# Create your models here.
class Categories_models(models.Model):
	categoriy =  models.CharField(max_length = 25, verbose_name = 'Котегория')
	photo     = models.ImageField(upload_to='categoriy/')

	class Meta():
		verbose_name = 'Котегория'
		verbose_name_plural = 'Котегории'

	def __str__(self):
		return self.categoriy

class Techer_models(models.Model):
	teacher_name      = models.CharField(max_length = 50)
	techer_p          = models.ImageField(upload_to = 'teachers/')
	teacher_info      = models.TextField()
	categoriy_teacher = models.ForeignKey(Categories_models, on_delete = models.CASCADE)

	class Meta():
		verbose_name = 'Учитель'
		verbose_name_plural = 'Учителя'

	def __str__(self):
		return self.teacher_name


class lesson_models(models.Model):
	photos  = models.ImageField(upload_to = 'lesson/')
	name    = models.CharField(max_length = 50)
	teacher = models.ForeignKey(Techer_models, on_delete = models.CASCADE)
	prise   = models.IntegerField()
	categoriy_lesson = models.ForeignKey(Categories_models, on_delete = models.CASCADE)

	class Meta():
		verbose_name = 'Урок'
		verbose_name_plural = 'Уроки'

	def __str__(self):
		return self.name

class Moduls_models(models.Model):
	lesson_type = models.ForeignKey(lesson_models, on_delete = models.CASCADE)
	moduls_l    = models.CharField(max_length = 100)

	class Meta():
		verbose_name = 'Модуль'
		verbose_name_plural = 'Модули'

	def __str__(self):
		return self.moduls_l


class thems_video_models(models.Model):
	Moduls_type = models.ForeignKey(Moduls_models, on_delete = models.CASCADE)
	video       = EmbedVideoField()  # same like models.URLField()
	info        = models.TextField(default="topilmadi")
	info_url    = models.CharField(max_length = 100)

	class Meta():
		verbose_name = 'Урок-видео'
		verbose_name_plural = 'Уроки-видео'

	def __str__(self):
		return f'видео:{self.Moduls_type}'
