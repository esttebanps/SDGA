from inventory.viewsets import CategoryViewSet,ProductViewSet
from sales.viewsets import SaleViewSet
from profiles.viewsets import SupplierViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register('category',CategoryViewSet)
router.register('product',ProductViewSet)
router.register('sale',SaleViewSet)
router.register('supplier',SupplierViewSet)