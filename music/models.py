from django.db import models
from django.utils.translation import gettext_lazy as _


class Artist(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=_('Artist'))

    class Meta:
        verbose_name = _('Artist')
        verbose_name_plural = _('Artists')
        ordering = ['name']

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Song title'))

    class Meta:
        verbose_name = _('Song')
        verbose_name_plural = _('Songs')
        ordering = ['title']

    def __str__(self):
        return self.title


class Album(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Album title'))
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name='albums', verbose_name=_('Artist')
    )
    release_year = models.PositiveIntegerField(verbose_name=_('Release year'))
    songs = models.ManyToManyField(Song, through='AlbumSong', related_name='albums', verbose_name=_('Songs'))

    class Meta:
        verbose_name = _('Album')
        verbose_name_plural = _('Albums')
        ordering = ['release_year', 'title']

    def __str__(self):
        return f'{self.title} ({self.release_year})'


class AlbumSong(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='album_songs')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='album_songs')
    track_number = models.PositiveIntegerField(verbose_name=_('Track number'))

    class Meta:
        verbose_name = _('Song in the album')
        verbose_name_plural = _('Songs in albums')
        unique_together = ('album', 'track_number')
        ordering = ['track_number']

    def __str__(self):
        return f'{self.track_number} - {self.song.title} ({self.album.title})'
