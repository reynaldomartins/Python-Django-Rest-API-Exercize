from rest_framework import serializers
from .models import TODOs

class TODOSerializer(serializers.ModelSerializer):
    class Meta:
        model = TODOs
        fields = ("id","td_state","td_duedate","td_text")
