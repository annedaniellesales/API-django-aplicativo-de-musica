from django.db import models
from uuid import uuid4
from artists.models import Artists


class Musics(models.Model):
    id_music = models.UUIDField(primary_key=True, default=uuid4,editable=False)
    name_music = models.CharField(max_length=255)
    Artist = models.ForeignKey(Artists,on_delete=models.CASCADE, related_name='artista',blank=False, null=True)

    class Meta:
        managed =True
        db_table = ('Musics')
        unique_together = ('name_music','Artist')
