
from django.contrib import admin
from django.urls import path
from apis import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('apis/', views.StudentList.as_view()),
    path('apis/', views.StudentCreate.as_view()),
    path('apis/<int:pk>/', views.StudentRetrieve.as_view()),
    # path('apis/<int:pk>/', views.StudentUpdate.as_view()),
    # path('apis/<int:pk>/', views.StudentDestroy.as_view()),
]


