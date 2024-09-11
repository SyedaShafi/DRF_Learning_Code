
from django.contrib import admin
from django.urls import path
from apis.views import StudentView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/',StudentView.as_view(), name='student_api'),
]
