from django.db.models import fields
from rest_framework import serializers

from artists.models import Artists
from artists.models import Artists

class ArtistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artists
        fields = "__all__"