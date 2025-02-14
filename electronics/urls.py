from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from electronics.apps import ElectronicsConfig
from electronics.views import NetworkNodeViewSet, UserRegistrationView

app_name = ElectronicsConfig.name

router = DefaultRouter()
router.register(r'', NetworkNodeViewSet)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('', include(router.urls)),
]
