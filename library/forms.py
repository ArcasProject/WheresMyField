from django import forms

class SearchForm(forms.Form):
    keywords = forms.CharField(label='What do you care about?', max_length=200)
