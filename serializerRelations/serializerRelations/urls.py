
from django.contrib import admin
from django.urls import path, include
from apis import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('singer', views.SingerViewSet)
router.register('song', views.SongViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]
