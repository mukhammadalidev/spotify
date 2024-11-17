from django.urls import path
from .views import SongListAPIView,SongDetailAPIView,SongSearchAPIView,PlayListAPIView,PlayListSongAPIView


urlpatterns = [
    path('all/',SongListAPIView.as_view(), name='song-lists'),
    path('detail/<int:pk>/', SongDetailAPIView.as_view(), name='song-list'),
    path('search/',SongSearchAPIView.as_view(), name='song-search'),
    path('playlist/',PlayListAPIView.as_view(), name='song-playlist'),
    path('playlist/song/', PlayListSongAPIView.as_view(), name='playlist-songs'),
]