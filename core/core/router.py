from inventory.viewsets import CategoryViewSet,ProductViewSet
from sales.viewsets import SaleViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register('category',CategoryViewSet)
router.register('product',ProductViewSet)
router.register('sale',SaleViewSet)