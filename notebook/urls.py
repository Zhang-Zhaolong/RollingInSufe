from django.urls import path
from . import views

app_name = 'notebook'
urlpatterns = [
    path('index', views.index, name='index'),
    path('<int:pk>', views.details, name='details'),
    path('materials/<int:pk>', views.materials, name='material'),
    # path('atc_tags/<int:pk>', views.tag, name='tag'),
]
