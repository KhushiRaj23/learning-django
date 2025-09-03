from django import forms
 
class InputForm(forms.Form):
    name= forms.CharField(min_length=3,max_length=6)
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    
    