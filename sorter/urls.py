from django.urls import path
from . import views

urlpatterns = [
    path('', views.sorting_view, name='sorting'),
]
