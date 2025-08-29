from rest_framework import viewsets

from .models import Artist, Album, Song
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.prefetch_related('albums__album_songs__song').all()
    serializer_class = ArtistSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.prefetch_related('album_songs__song', 'artist').all()
    serializer_class = AlbumSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
