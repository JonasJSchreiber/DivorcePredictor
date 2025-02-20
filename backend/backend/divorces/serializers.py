from rest_framework.serializers import ModelSerializer
from .models import DivorceCase


class DivorceCaseSerializer(ModelSerializer):
    class Meta:
        model = DivorceCase
        exclude = ("id", "is_divorced")
