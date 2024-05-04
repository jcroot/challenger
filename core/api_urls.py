from django.urls import re_path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from traffic.views import ChargeViolationView

PREFIX = "api"

router = routers.DefaultRouter()

urlpatterns = [
    re_path(f"{PREFIX}/", include(router.urls)),

    re_path(r'cargar_infraccion', ChargeViolationView.as_view({
        'post': 'charge_violation',
    }), name='charge_violation'),
    re_path(r'generar_reporte', ChargeViolationView.as_view({
        'get': 'generate_report',
    }), name='generate_report'),

    # JWT
    re_path(r'token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(r'token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]