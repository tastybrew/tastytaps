from django.conf.urls import include, url

from .views import HomePageView


urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^api/v1/', include('tastytaps.taps.urls', namespace='v1')),
]
