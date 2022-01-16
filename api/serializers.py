from rest_framework.serializers import ModelSerializer
from .models import Data


class the_ModelSerializer(ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'
