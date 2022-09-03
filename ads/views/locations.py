from rest_framework.viewsets import ModelViewSet
from ads.models_old import Location
from ads.serializers.location import LocationSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
