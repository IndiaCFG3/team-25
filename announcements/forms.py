from django import forms
from qna.models import ClassRoom

class AnnouncementForm(forms.Form):
    classroom = forms.ModelChoiceField(queryset=ClassRoom.objects.all().order_by('id'))
    title = forms.CharField(max_length=200)
    link = forms.URLField()
    body = forms.CharField(max_length=200)

