

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apis import views
router = DefaultRouter()
router.register('singer', views.SingerViewset )
router.register('song', views.SongViewset )
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
