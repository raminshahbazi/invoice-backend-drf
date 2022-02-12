from core.views import ItemViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'items', ItemViewSet, basename='items')

urlpatterns = [] + router.urls
