from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from api.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url('^admin/', admin.site.urls),
    url(r'^auth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
