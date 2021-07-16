from rest_framework import serializers
from address.models import Country, State, City

class CitySerializer(serializers.ModelSerializer):

    # id = serializers.IntegerField(required=False)
    # sub_cateory_name = serializers.SerializerMethodField()

    class Meta:
        model = City
        # fields = '__all__'
        fields = ['id', 'name']

class StateSerializer(serializers.ModelSerializer):

    # id = serializers.IntegerField(required=False)
    # sub_cateory_name = serializers.SerializerMethodField()
    city = CitySerializer(many=True, required=False)

    class Meta:
        model = State
        # fields = '__all__'
        fields = ['id', 'name', 'city']

class CountrySerializer(serializers.ModelSerializer):

    # id = serializers.IntegerField(required=False)
    # sub_cateory_name = serializers.SerializerMethodField()
    state = StateSerializer(many=True, required=False)

    class Meta:
        model = Country
        # fields = '__all__'
        fields = ['id', 'name', 'state']