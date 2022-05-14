from django.forms import ModelForm

from mainapp.models import Diary


class DiaryForm(ModelForm):
    class Meta:
        model = Diary
        fields = ['diary_content', 'diary_date', 'diary_img']