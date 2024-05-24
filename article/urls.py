from django.urls import path
from . import views

app_name = 'article'
urlpatterns = [
    path('index', views.index, name='index'),
    path('<int:pk>', views.details, name='details'),
    path('atc_tags/<int:pk>', views.tag, name='tag'),
]