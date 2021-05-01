from django.urls import path
from profile_api.views import HelloApiView

urlpatterns = [
    path('hello', HelloApiView.as_view(), name='hello'),
]
