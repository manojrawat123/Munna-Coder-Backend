from django.shortcuts import render
from rest_framework.views import APIView 
from visitor_tracer.models import Visitor
from rest_framework.response import Response
from rest_framework import status
from visitor_tracer.models import Visitor
from visitor_tracer.serializer import VisitorSerializer
from django.core.mail import send_mail ,EmailMessage  
from django.conf import settings


# Create your views here.
class UserTracerView(APIView):
    def post(self, request, id=None):
        subject = "SomeOne Visited Your Website"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["positive.mind.123456789@gmail.com"]
        try:
            if id is not None:
                return Response({"error": "Some Error Occured"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
            else:
                visitor_serializer = VisitorSerializer(data = request.data)
                if visitor_serializer.is_valid():
                    visitor_serializer.save()
                    ip_adress = request.data.get("sup_id_adress")
                    message = f"Hii user With Ip adress {ip_adress} Visit Your website"
                    email = EmailMessage(subject, message, email_from, recipient_list)
                    email.send() 
                    return Response({"msg": "Ip Adress Come"}, status=status.HTTP_200_OK)
                else:
                    email = EmailMessage(subject, "Hii Annmoyus User Visit Your website", email_from, recipient_list)
                    email.send()
                    return Response({"msg": "Annmoyus User"}, status=status.HTTP_200_OK)
                    

        except Exception as e:
            print(e)
            email = EmailMessage(subject, "Hii Internal Server Error while user visit", email_from, recipient_list)
            email.send()
            return Response({"error": "Some Error Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            