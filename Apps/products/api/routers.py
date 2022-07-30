from rest_framework.routers import DefaultRouter
from Apps.products.api.Views.products_views import productViewSet


router = DefaultRouter()
router.register(r'products', productViewSet, basename='products')
urlpatterns = router.urls