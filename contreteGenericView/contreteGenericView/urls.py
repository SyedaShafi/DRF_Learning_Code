
from django.contrib import admin
from django.urls import path
from apis import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis/', views.StudentListAndCreate.as_view()),
    path('apis/<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view()),
]


