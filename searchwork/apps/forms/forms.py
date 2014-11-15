# coding: utf-8
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth import login
from django.utils.translation import ugettext as _

WHO = (('работа датель', 'Работа датель'),
	('работник','Работник'))

class Reg(forms.ModelForm):
	password1 = forms.CharField(widget=forms.PasswordInput())
	password2 = forms.CharField(widget=forms.PasswordInput())
	town = forms.CharField(max_length=200)
   	who = forms.MultipleChoiceField(required=False,
        widget=forms.CheckboxSelectMultiple, choices=WHO)
	class Meta:

		model = User
		fields = ('first_name', 'last_name', 'email', 'username')

	def clean_password2(self):
		password1 = self.cleaned_data['password1']
		password2 = self.cleaned_data['password2'] 
		if password1 == password2:
			pass
		else:
			raise forms.ValidationError("Пароль не совпадает")







	



	



