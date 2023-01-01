from django.urls import path

from . import views

app_name = 'game'

urlpatterns = [
    path('playgame/<name>/', views.playGame, name='playgame'),
    path('getHighScore/', views.getHighScore, name='getHighscore'),
    path('setHighScore/<score>/<name>/', views.setHighScore, name='getHighScore'),
]
