from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('task1/',views.task1,name='task1'),
    path('task2/',views.task2,name='task2'),
path('task3/',views.task3,name='task3'),
]
