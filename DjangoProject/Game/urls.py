from django.urls import path

from . import views

app_name = 'agile'

urlpatterns = [
    path('playgame/', views.playGame, name='playgame'),
]
