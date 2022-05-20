from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

from mainapp.models import Diary


def create_diary(request):

    # 처음으로 생성할 경우
    if request.method == "POST":
        print('hello')
        diary_img = request.FILES['diary_img']
        diary_content = request.POST.get('diary_content')
        diary_share_state = False

        diary = Diary()

        diary.diary_img = diary_img
        diary.diary_content = diary_content
        diary.diary_share_state = diary_share_state
        diary.save()

        return render(request, template_name='diaryapp/create.html', context={})

    if request.method == 'GET':
        print('get')
        return render(request, template_name='diaryapp/create.html', context={})

    else:
        print("no!")
        return render(request, template_name='diaryapp/create.html', context={})

