from django.contrib import admin
from django.urls import path, include
from apis import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from apis import customAuth
# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('apis', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('gettoken/', obtain_auth_token),
    path('gettoken/', customAuth.CustomAuthToken.as_view()),
    path('auth/', include('rest_framework.urls'), name = "rest_framework"),
]
        
