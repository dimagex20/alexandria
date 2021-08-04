from django.urls import include, path, re_path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
# router.register(r'api_test', views.TestViewSet)

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^test/$', views.TestViewSet.as_view()),
    re_path(r'^test/(?P<name>[0-9a-zA-Z_-]+)', views.TestViewSet.as_view())
]
