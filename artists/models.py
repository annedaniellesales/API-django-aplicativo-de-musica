from django.db import models
from uuid import uuid4

class Artists(models.Model):
    id_artist = models.UUIDField(primary_key=True, default=uuid4,editable=False)
    Artist= models.CharField(max_length=255)
    Style = models.CharField(max_length=255)

    class Meta:
        managed =True
        db_table = ('Artists')
        unique_together = ('Artist', 'Style')