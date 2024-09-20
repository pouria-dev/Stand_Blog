from django import forms

class Contact_Form(forms.Form):
    name = forms.CharField(max_length=10 , label="Name")
    text = forms.CharField(widget=forms.Textarea)
