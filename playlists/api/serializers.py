from django.db.models import fields
from rest_framework import serializers

from playlists.models import Playlists


class PlaylistsSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Playlists
        fields = '__all__'