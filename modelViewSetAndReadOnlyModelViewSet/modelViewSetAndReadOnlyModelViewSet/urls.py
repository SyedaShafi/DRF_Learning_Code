from django.contrib import admin
from django.urls import path, include
from apis import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('apis', views.StudentModelViewSet, basename='student')
router.register('readOnly', views.StudentModelViewSetReadOnly, basename='studentreadonly')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
        
        