from rest_framework import serializers
from facilities.models import Facility


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ('name', 'address', 'code', 'email', 'providers')
