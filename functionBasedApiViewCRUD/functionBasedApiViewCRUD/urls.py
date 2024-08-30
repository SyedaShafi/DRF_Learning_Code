
from django.contrib import admin
from django.urls import path
from apis import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis/', views.student_apis),
    path('apis/<int:id>/', views.student_apis),
]
