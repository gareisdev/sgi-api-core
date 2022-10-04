from django.urls import include, path
from rest_framework import routers
from authentication.api.viewsets import LoginViewSet

router = routers.DefaultRouter()

router.register("login", LoginViewSet, basename="login")

urlpatterns = [path("", include(router.urls))]
