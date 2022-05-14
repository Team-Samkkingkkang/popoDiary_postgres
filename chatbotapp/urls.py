from django.urls import path
from django.views.generic import TemplateView

app_name = "chatbots"

urlpatterns = [
    path('chatbot/', TemplateView.as_view(template_name='chatbotapp/chatbot.html'), name="chatbot")
]