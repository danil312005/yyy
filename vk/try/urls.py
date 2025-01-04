from django.urls import path
from . import views

urlpatterns = [
    path('button/', views.button_page, name='button_page'),
]
