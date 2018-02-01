from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth.views import login, logout
from django.views.generic.base import RedirectView
from rest_framework import routers
from api.views import UserViewSet
from consumer.views import ConsumerView, ConsumerExchangeView, ConsumerDoneView
from rest_framework.documentation import include_docs_urls
from rest_framework.permissions import AllowAny

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='user')

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='consumer')),
    url(r'^docs', include_docs_urls(
        title='User API', permission_classes=[AllowAny]
    )),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, {'next_page': '/consumer'}, name='logout'),
    url(r'^api/', include(router.urls)),
    url(r'^auth/', include(
        'oauth2_provider.urls', namespace='oauth2_provider'
    )),
    url(r'^consumer/$', ConsumerView.as_view()),
    url(
        r'^consumer/exchange/',
        ConsumerExchangeView.as_view(),
        name='consumer-exchange'
    ),
    url(r'^consumer/done/', ConsumerDoneView.as_view(), name='consumer-done')
]
