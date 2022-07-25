from django import forms
from .models import character, User
from django.forms import modelform_factory

#class CharacterForm (forms.ModelForm):
    #character_name = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))

    #class Meta:
        #model = character
        #fields = '__all__'

CharacterForm = modelform_factory(character, exclude=('author',))