from django.urls import path
from .import views


urlpatterns = [
    path('contacts/', views.Contacts.as_view()),
    path('about/', views.About.as_view()),
    path('categories/', views.categories, name='categories'),
    #path('regions/', views.regions, name='regions')
]