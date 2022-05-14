from django.urls import path
from django.views.generic import TemplateView

app_name = "mys"

urlpatterns = [
    path('my/', TemplateView.as_view(template_name='myapp/myapp.html'), name="my")
]
