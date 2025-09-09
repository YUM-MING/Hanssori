from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recommend/', views.recommend_view, name='recommend_view'),  # 추천 결과
    path("playlist/", views.playlist_view, name="playlist_view"),  # 곡 플레이어
]
