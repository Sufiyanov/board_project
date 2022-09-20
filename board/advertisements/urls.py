from django.urls import path
from .import views

urlpatterns = [
    path('', views.Home.as_view()),
    path('advertisement/', views.advertisement_detail, name='advertisement_detail'),
    path('advertisement/courses_list', views.courses_list, name='courses_list'),
    path('advertisement/course_1', views.course_1, name='course_1'),
    path('advertisement/course_2', views.course_2, name='course_2'),
    path('advertisement/course_3', views.course_3, name='course_3'),
    path('advertisement/course_4', views.course_4, name='course_4'),
    path('regions/', views.Regions.as_view())
]