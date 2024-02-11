from django import forms
from .models import Grade, Subject

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['subject', 'marks']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subject'].queryset = Subject.objects.all()