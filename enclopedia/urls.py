from django.urls import path

from enclopedia import views

urlpatterns = [
    path('say-hi/<str:name>', views.say_hi, name='say-hhi'),
    path('', views.index, name='index'),
    ]