from django import forms


class SampleFormClass(forms.Form):
    welcome_text = forms.CharField(max_length=100)
