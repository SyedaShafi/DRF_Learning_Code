
from django.contrib import admin
from django.urls import path
from apis import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.StudentList.as_view()),
]
