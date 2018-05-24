from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label="your name", max_length=100)
    message = forms.CharField(widget=forms.Textarea)
