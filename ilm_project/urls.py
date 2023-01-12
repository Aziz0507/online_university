from django.contrib import admin
from django.urls import path
from ilm_pages.views import Main_views, Corses_view, Thems_view, SQL_lesson_view,Lesson_video_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', Main_views.as_view(), name = 'main'),
    path('corses/<int:pk>/', Corses_view.as_view(), name = 'corses'),
    path('thems/<int:pu>/', Thems_view.as_view(), name = 'thems'),
    path('videos/<int:slug>/', Lesson_video_view.as_view(), name = 'videos'),
    path('sql_lesson/',SQL_lesson_view, name = 'sql'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
