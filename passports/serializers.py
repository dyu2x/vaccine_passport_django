from rest_framework import serializers
from passports.models import Passport


class PassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passport
        fields = ('date_administered', 'provider', 'facility')
