from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList, PostsDetail


urlpatterns = [
   path('', PostsList.as_view()),
   path('<int:pk>', PostsDetail.as_view()),
]
