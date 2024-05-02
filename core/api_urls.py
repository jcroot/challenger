from django.urls import re_path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

PREFIX = "api"

router = routers.DefaultRouter()

urlpatterns = [
    re_path(f"{PREFIX}/", include(router.urls)),

    # JWT
    re_path(r'token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(r'token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]