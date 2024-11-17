from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from song.models import Song, PlayList, PlayListSong
from song.serializers import SongSerializer, PlayListSerializer, PlayListSongSerializer


# Create your views here.
class SongListAPIView(APIView):

    def get(self,request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)



class SongDetailAPIView(APIView):
    def get(self,request,pk):
        song = Song.objects.get(pk=pk)
        serializer = SongSerializer(song)
        return Response(serializer.data)


class SongSearchAPIView(APIView):
    def get(self,request):
        search_query = request.GET.get('q',None)
        if search_query:
            songs = Song.objects.filter(title__icontains=search_query)
        else:
            songs = Song.objects.all()

        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)


class PlayListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        playlist = PlayList.objects.filter(user=request.user)
        serializer = PlayListSerializer(playlist,many=True)
        return Response(serializer.data)


    def post(self,request):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = PlayListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlayListDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        playlist = PlayList.objects.get(pk=pk)
        serializer = PlayListSerializer(playlist,many=True)
        return Response(serializer.data)


class PlayListSongAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        song = PlayListSong.objects.filter(user=request.user)
        serializer = PlayListSongSerializer(song,many=True)
        return Response(serializer.data)
