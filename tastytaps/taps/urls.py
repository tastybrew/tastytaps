from rest_framework import routers

from . import views


router = routers.SimpleRouter()
router.register(r'beers', views.BeersViewSet)


urlpatterns = router.urls
