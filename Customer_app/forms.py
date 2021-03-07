from django import forms
from Customer_app.models import Customer_Model


gen = (('MALE', 'male'),('FEMALE', 'female'),('OTHERS','others'))
class Customer_Form(forms.ModelForm):
    u_gender = forms.ChoiceField(choices=gen,widget=forms.RadioSelect)
    u_address = forms.CharField(widget=forms.TextInput)
    u_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Customer_Model
        fields= "__all__"