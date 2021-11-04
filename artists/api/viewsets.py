from rest_framework import serializers, viewsets
from artists.api.serializers import ArtistsSerializer
from artists.models import Artists

class ArtistsViewsets(viewsets.ModelViewSet):
    serializer_class = ArtistsSerializer
    queryset = Artists.objects.all()