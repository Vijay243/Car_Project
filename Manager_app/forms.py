from django import forms
from .models import Car_Model,Driver_Model

gen = (('MALE', 'male'), ('FEMALE', 'female'), ('OTHERS', 'others'))
class Driver_Form(forms.ModelForm):
    d_gender = forms.ChoiceField(choices=gen,widget=forms.RadioSelect)
    Address = forms.CharField(widget=forms.TextInput)
    class Meta:
        model = Driver_Model
        fields = "__all__"

class Car_Form(forms.ModelForm):
    class Meta:
        model = Car_Model
        fields = "__all__"