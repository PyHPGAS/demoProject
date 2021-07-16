from django.shortcuts import render
from myusers.models import UserProfile
from myusers.serializers import UserProfileSerializer
from rest_framework import viewsets
# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    serializer_class = UserProfileSerializer

    def get_queryset(self):

        try:
            return UserProfile.objects.all()
        except Exception as err:
            return {}

# Create your views here.
