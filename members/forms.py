

from django import forms
from members.models import Members
class MembersForm(forms.ModelForm):

    # firstname = forms.CharField(max_length=255)
    # lastname = forms.CharField(max_length=255)
    # age = forms.IntegerField()

    class Meta:
        model = Members
        # fields = '__all__'
        fields = ['firstname', 'lastname']

