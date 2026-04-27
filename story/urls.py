from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/map-data/', views.map_data, name='map_data'),
]
