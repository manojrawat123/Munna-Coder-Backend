from django.shortcuts import render
from rest_framework.views import APIView
from my_contact.models import Contact
from my_contact.seriailzer import ContactSerializer
from rest_framework.response import Response
from rest_framework import status 
from django.conf import settings
from django.core.mail import send_mail ,EmailMessage  


# Create your views here.
class ContactLogView(APIView):
    def post(self, request):
        contact_serializer = ContactSerializer(data=request.data)
        try: 
            if contact_serializer.is_valid():
                email_from = settings.EMAIL_HOST_USER
                name = request.data['name']
                user_email =  request.data['email']
                phone =  request.data['phone']
                body =  request.data['message']
                subject = f"New Contact Form Submission from {name}"
                message = f'''Name: {name}
                        Email: {user_email}
                        Phone: {phone}
                        Message:{body}'''
                recipient_list= ["positive.mind.123456789@gmail.com"]
                email = EmailMessage(subject, message, email_from, recipient_list)
                print(name, email, body, phone)
                email.send()
                contact_serializer.save()
                return Response({"msg": "Message Send Sucessfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Some Error Occured"}, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            print(e)
            return Response({"error": "Some Error Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)