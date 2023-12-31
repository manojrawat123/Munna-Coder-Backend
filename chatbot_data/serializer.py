from rest_framework import serializers
from chatbot_data.models import ChatBotData

class ChatBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatBotData
        fields = "__all__"