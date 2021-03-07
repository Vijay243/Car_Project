from django import forms
from .models import Manager_Model

gen = (('MALE', 'male'),('FEMALE', 'female'),('OTHERS','others'))
class Manager_Form(forms.ModelForm):
    gender = forms.ChoiceField(choices=gen,widget=forms.RadioSelect)
    Address = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Manager_Model
        fields = "__all__"
