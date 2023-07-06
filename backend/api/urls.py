from rest_framework import permissions, routers
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from api.views import generate_test_data, load_data, get_status
from api.tasks import task_task

# schema_view = get_schema_view(
#    openapi.Info(
#       title="Wallet API",
#       default_version='v1',
#       description="Pet project for learning Django and Django Rest Framework",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="perm300ru@yandex.ru"),
#       license=openapi.License(name="MIT License"),
#    ),
#    public=True,
#    permission_classes=[permissions.AllowAny],
# )

app_name = 'api'

urlpatterns = [
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('tasks/', task_task, name='task_task'),
    path('generate_test_data/', generate_test_data, name='generate_test_data'),
    path('load-data/', load_data, name='load_data'),
    path('status/<str:task_id>/', get_status, name='get_status'),
]
