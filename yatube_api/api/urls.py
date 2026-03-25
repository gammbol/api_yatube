from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as token_views
from . import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='posts')
router.register(r'groups', views.GroupViewSet, basename='groups')

urlpatterns = [
    path('v1/api-token-auth/', token_views.obtain_auth_token, name='api_token_auth'),
    path('v1/', include(router.urls)),
]