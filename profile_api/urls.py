from django.urls import path, include
from profile_api.views import HelloApiView, HelloViewsets, UserProfileViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', HelloViewsets, basename='hello-viewset')
router.register('profile', UserProfileViewset)

urlpatterns = [
    path('hello', HelloApiView.as_view(), name='hello'),
    path('', include(router.urls)),
]
