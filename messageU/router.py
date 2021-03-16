from core.api.viewsets import ClientViewSet,MessegeViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('client', ClientViewSet)
router.register('message', MessegeViewSet)
