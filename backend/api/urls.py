from rest_framework import permissions, routers
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from api.views import WalletViewSet, AccountViewSet, TransactionViewSet, OperationViewSet, AttachmentViewSet

router = routers.DefaultRouter()
router.register(r'wallets', WalletViewSet)
router.register(r'accounts', AccountViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'operations', OperationViewSet)
router.register(r'attachments', AttachmentViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Wallet API",
      default_version='v1',
      description="Pet project for learning Django and Django Rest Framework",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="perm300ru@yandex.ru"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

app_name = 'api'

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include(router.urls)),
]
