from django import forms
from . models import *


class FormcallForm(forms.ModelForm):
	class Meta:
		model = Formcall
		exclude = ['']
		