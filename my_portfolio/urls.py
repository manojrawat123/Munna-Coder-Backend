"""my_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from my_projects.views import MyProjectView
from my_contact.views import ContactLogView
from visitor_tracer.views import UserTracerView
from chatbot_data.views import ChatBotDataView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', MyProjectView.as_view(),name="project"),
    path('contact/', ContactLogView.as_view(),name="contact"),
    path('visitor/',UserTracerView.as_view(), name="visitor"),
    path('chatbot/',ChatBotDataView.as_view(), name="chat_bot"),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
