from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from lattices.api.serializers import LatticesSerializer
from lattices.models import Lattices


class LatticesViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LatticesSerializer
    queryset = Lattices.objects.all()


class PublicLatticesViewSet(ModelViewSet):
    http_method_names = ['get']
    serializer_class = LatticesSerializer
    queryset = Lattices.objects.all()
