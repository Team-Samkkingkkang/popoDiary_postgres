from django.urls import path
from django.views.generic import TemplateView

from diaryapp import views

app_name = "diarys"

urlpatterns = [
    path('', TemplateView.as_view(template_name='diaryapp/diary.html'), name="diary"),
    path('create/', views.create_diary, name="create_diary")
]
