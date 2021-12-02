from django import forms
from django.forms import widgets
from .models import Poem

class PoemForm(forms.ModelForm):

    class Meta:
        model = Poem
        fields = ('name', 'title', 'body')

        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'What is your name?', 'label':''}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'title', 'placeholder': 'What is your poem called?'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'id': 'textAreaBody', 'placeholder': 'Type your poem here...'})

        }

class UpdatePoemForm(forms.ModelForm):

    class Meta:
        model = Poem
        fields = ('name', 'title', 'body')

        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'What is your name?', 'label':''}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'title', 'placeholder': 'What is your poem called?'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'id': 'textAreaBody', 'placeholder': 'Type your poem here...'})

        }