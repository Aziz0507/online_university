from django.contrib import admin
from .models import Categories_models, Techer_models, lesson_models, Moduls_models, thems_video_models


from embed_video.admin import AdminVideoMixin


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Categories_models)
admin.site.register(Techer_models)
admin.site.register(lesson_models)
admin.site.register(Moduls_models)
admin.site.register(thems_video_models, MyModelAdmin)


