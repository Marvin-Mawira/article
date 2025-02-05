from django.urls import path, include
# from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.contrib import admin
from articles import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    # path('<int:id>/', views.article_detail, name='article_detail'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    path('create/', views.article_create, name='article_create'),
    path('<int:id>/update/', views.article_update, name='article_update'),
    path('<int:id>/delete/', views.article_delete, name='article_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

