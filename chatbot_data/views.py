from django.shortcuts import render
from rest_framework.views import APIView
from chatbot_data.serializer import ChatBotSerializer
from rest_framework.response import Response
from rest_framework import status 
from django.conf import settings
from django.core.mail import send_mail ,EmailMessage  


# Create your views here.
class ChatBotDataView(APIView):
    def post(self, request):
        chatbot_serializer = ChatBotSerializer(data=request.data)
        try: 
            if chatbot_serializer.is_valid():
                chatbot_serializer.save()
                return Response({"msg": "Message Send Sucessfully"}, status=status.HTTP_200_OK)
            else:
                return Response(chatbot_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({"error": "Some Error Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)