from rest_framework import serializers

from .models import Artist, Album, Song, AlbumSong


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title']


class AlbumSongSerializer(serializers.ModelSerializer):
    song = SongSerializer()

    class Meta:
        model = AlbumSong
        fields = ['track_number', 'song']


class AlbumSerializer(serializers.ModelSerializer):
    artist = serializers.StringRelatedField()
    album_songs = AlbumSongSerializer(many=True)

    class Meta:
        model = Album
        fields = ['id', 'title', 'artist', 'release_year', 'album_songs']


class ArtistSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True)

    class Meta:
        model = Artist
        fields = ['id', 'name', 'albums']
