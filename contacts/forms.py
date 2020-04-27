from .models import Contact
from phonenumber_field.formfields import PhoneNumberField
from django import forms

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length= 50, widget=forms.TextInput(attrs={'class': "form-control"}) )
    email = forms.EmailField(max_length=200,widget=forms.TextInput(attrs={'class': "form-control",'id': "clientemail"}))
    message = forms.CharField( widget=forms.Textarea(attrs={'class': "form-control"}))
    subject = forms.CharField( widget=forms.TextInput(attrs={'class': "form-control"}))
    phonenumber = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': ('Phone')}),label=("Phone number"), required=False)
  
    class Meta:
        model = Contact
        fields = ('name','email','subject','phone','message',)