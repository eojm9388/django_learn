from django import forms
from .models import Diray

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diray
        fields = '__all__'

        