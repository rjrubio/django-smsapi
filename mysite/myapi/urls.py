from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'sms', views.SmViewSet)
router.register(r'devices', views.DeviceViewSet)
router.register(r'college', views.CollegeViewSet)
router.register(r'meta', views.MetaViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('hey/', views.hey),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('fcmPush/', views.fcmPush),
]