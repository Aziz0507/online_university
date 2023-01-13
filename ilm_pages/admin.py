from django.contrib import admin
from .models import Categories_models, Techer_models, lesson_models, Moduls_models, thems_video_models


from embed_video.admin import AdminVideoMixin


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

class Admin_sortirovka_lesson_models(admin.ModelAdmin):
    list_display  = ('name', 'teacher', 'categoriy_lesson',)

class Admin_sortirovka_Moduls_models(admin.ModelAdmin):
    list_display  = ('moduls_l', 'lesson_type',)

class Admin_sortirovka_Techer_models(admin.ModelAdmin):
    list_display  = ('teacher_name', 'categoriy_teacher',)

# Register your models here.
admin.site.register(Categories_models)
admin.site.register(Techer_models, Admin_sortirovka_Techer_models)
admin.site.register(lesson_models, Admin_sortirovka_lesson_models)
admin.site.register(Moduls_models,Admin_sortirovka_Moduls_models)
admin.site.register(thems_video_models, MyModelAdmin)


