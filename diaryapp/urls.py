from django.urls import path
from django.views.generic import TemplateView

app_name = "diarys"

urlpatterns = [
    path('diary/', TemplateView.as_view(template_name='diaryapp/diary.html'), name="diary")
]
