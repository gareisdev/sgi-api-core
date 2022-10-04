from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from django.contrib.auth.models import User

from authentication.api.serializers import UserLoginSerializer, UserModelSerializer


class LoginViewSet(viewsets.GenericViewSet):

    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=["post"])
    def login(self, request):

        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()

        data = {"user": UserModelSerializer(user).data, "access_token": token}

        return Response(data, status=status.HTTP_201_CREATED)
