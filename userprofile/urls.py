from django.urls import path
from . import views

app_name = 'userprofile'
urlpatterns = [
    path('<int:pk>', views.profiles, name='profiles'),
    path('wordcloud/<int:pk>', views.wordcloud, name='wordcloud'),
]
