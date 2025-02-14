from rest_framework import viewsets
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from electronics.models import NetworkNode
from electronics.serializers import NetworkNodeSerializer, UserRegistrationSerializer
from electronics.permissions import IsActiveStaff
from rest_framework.permissions import AllowAny, IsAuthenticated


class NetworkNodeViewSet(viewsets.ModelViewSet):
    """ API для управления звеньями сети. """

    queryset = NetworkNode.objects.select_related("supplier").all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveStaff, IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["country"]


class UserRegistrationView(generics.CreateAPIView):
    """ API для регистрации пользователей. """

    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
