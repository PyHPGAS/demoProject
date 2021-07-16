from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myusers import views

router = DefaultRouter()
router.register(r'userprofile', views.UserProfileViewSet, basename="api_userprofiles")

urlpatterns = [
    path('', include(router.urls)),
]
