from django.conf.urls import include, url
from django.contrib import admin

from .views import HomePageView


urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
]
