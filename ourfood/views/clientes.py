from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from ourfood.models import Cliente
from ourfood.serializers import ClienteSerializer

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
        # return Response(serializer.data)
