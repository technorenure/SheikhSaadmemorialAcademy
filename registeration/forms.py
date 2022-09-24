from dataclasses import fields
from django.forms import ModelForm
from .models import ScoreSheet, Student

class ScoreForm(ModelForm):
    class Meta:
        model = ScoreSheet
        fields = '__all__'

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
