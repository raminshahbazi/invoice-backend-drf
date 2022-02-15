from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from core.views import ItemViewSet, InvoiceViewSet, user_info
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'items', ItemViewSet, basename='items')
router.register(r'invoices', InvoiceViewSet, basename='invoices')

urlpatterns = [
    path("login/", obtain_auth_token, name="obtain-auth-token"),
    path("user-info/", user_info, name="user-info"),
    # path("test/", Test.as_view({'get': 'list'}), name="test")
] + router.urls
