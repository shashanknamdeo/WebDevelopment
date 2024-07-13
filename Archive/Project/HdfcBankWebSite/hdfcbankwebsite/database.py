from django import forms

class login(forms.Form):
	Customer_ID = forms.IntegerField()
	password = forms.CharField()
