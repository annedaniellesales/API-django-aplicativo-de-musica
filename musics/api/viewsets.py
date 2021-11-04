from rest_framework import viewsets
from musics.models import Musics
from musics.api.serializers import MusicsSerializer

class MusicsViewSets(viewsets.ModelViewSet):
    serializer_class = MusicsSerializer
    queryset= Musics.objects.all()