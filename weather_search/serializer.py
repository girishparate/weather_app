from .models import SearchHistory
from rest_framework.serializers import ModelSerializer

class SearchHistorySerializer(ModelSerializer):
    class Meta:
        model = SearchHistory
        fields = '__all__'