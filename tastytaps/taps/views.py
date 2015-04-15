from rest_framework.permissions import IsAuthenticated

from .models import Taps
from .serializers import TapsSerializer

from rest_framework.viewsets import ModelViewSet


class TapsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Taps.objects.all()
    serializer_class = TapsSerializer
