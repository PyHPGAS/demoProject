from rest_framework import serializers
from myusers.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):

    # id = serializers.IntegerField(required=False)
    # sub_cateory_name = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = '__all__'
        # fields = ['id', 'name']