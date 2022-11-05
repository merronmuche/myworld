

from django import forms

class MembersForm(forms.Form):

    firstname = forms.CharField(max_length=255)
    lastname = forms.CharField(max_length=255)
    age = forms.IntegerField()

