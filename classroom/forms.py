from django import forms
from classroom.models import Resource

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = "__all__"
