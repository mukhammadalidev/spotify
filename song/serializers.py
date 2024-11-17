from rest_framework import serializers

from song.models import Song,Artist,PlayListSong,PlayList,Genre
from users.models import CustomUser
from users.serializers import UserSerializer


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class  PlayListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email')

class PlayListSerializer(serializers.ModelSerializer):
    user = PlayListUserSerializer(read_only=True)
    class Meta:
        model = PlayList
        fields = [ 'title', 'description','user','created_at']
        read_only_fields = ['user', 'created_at']




class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    genre=GenreSerializer()
    artist=ArtistSerializer()

    class Meta:
        model = Song
        fields = '__all__'


class PlayListSongSerializer(serializers.ModelSerializer):
    playlist = PlayListSerializer()
    user = PlayListUserSerializer(read_only=True)
    song = SongSerializer(read_only=True)
    class Meta:
        model = PlayListSong
        fields = '__all__'