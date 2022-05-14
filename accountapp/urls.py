from django.urls import path
from django.views.generic import TemplateView

app_name = "accounts"

urlpatterns = [
    path('hello/', TemplateView.as_view(template_name='accountapp/hello.html'), name="hello"),
    path('login/', TemplateView.as_view(template_name='accountapp/hello.html'), name="login")
]
