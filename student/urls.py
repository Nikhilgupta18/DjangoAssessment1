from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('getStudents/', views.getStudents),
    path('createStudent/', views.createStudent),
    path('getSections/', views.getSections),
    path('createSection/', views.createSection),
    path('getSectionWiseStudent/<str:section>', views.getSectionWiseStudent),
    path('updateSection/<int:pk>', views.updateSection),
    path('updateStudent/<int:pk>', views.updateStudent)

]
