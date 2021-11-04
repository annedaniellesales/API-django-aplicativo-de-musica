from django.db.models import fields
from rest_framework import serializers
from musics.models import Musics

class MusicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musics
        fields = "__all__"
    