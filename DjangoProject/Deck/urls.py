from django.urls import path

from . import views

app_name = 'deck'

urlpatterns = [
    path('generateCards/', views.generateCards, name='generateCards'),
]
