from rest_framework.viewsets import ModelViewSet
from ourfood.models import Administrador
from ourfood.serializers import AdministradorSerializer

class AdministradorViewSet(ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer

