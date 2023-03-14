from rest_framework.routers import DefaultRouter
from products.viewsets import ProductGenericViewSet

router = DefaultRouter()
router.register('products', ProductGenericViewSet, basename='products')

print("""📗   \x1b[1;34;40mrouters.py:7 router.urls:""") ## DELETEME
print(router.urls) ## DELETEME
print('\x1b[0m') ## DELETEME
urlpatterns = router.urls
