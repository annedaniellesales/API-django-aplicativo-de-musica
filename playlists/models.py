from django.db import models
from django.db.models import manager

from musics.models import Musics


class Playlists(models.Model):
    id_playlist = models.AutoField(primary_key=True)
    name_playlist =models.CharField(max_length=255)
    Music = models.ForeignKey(Musics, on_delete=models.CASCADE,related_name='playlists',blank=False,null = False)

    class Meta:
        managed = True
        db_table = 'playlists'
        unique_together = ('name_playlist','Music')

    

