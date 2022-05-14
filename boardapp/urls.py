from django.urls import path
from django.views.generic import TemplateView

app_name = "boards"

urlpatterns = [
    path('board/', TemplateView.as_view(template_name='boardapp/board.html'), name="board")
]
