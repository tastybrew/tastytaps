from rest_framework import routers

from . import views


router = routers.SimpleRouter()
router.register(r'taps', views.TapsViewSet)


urlpatterns = router.urls
