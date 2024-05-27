from django.urls import path
from . import views

app_name = 'map'
urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('select_crop', views.select_crop, name='select_crop'),
    path('mapPrice/', views.map_price, name='map_price'),
]