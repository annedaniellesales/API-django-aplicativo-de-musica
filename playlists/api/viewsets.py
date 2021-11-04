from rest_framework import viewsets
from playlists.models import Playlists
from playlists.api.serializers import PlaylistsSeriallizer
 


class PlaylistsViewSets(viewsets.ModelViewSet):
    queryset = Playlists.objects.all().order_by('name_playlist')
    serializer_class = PlaylistsSeriallizer
