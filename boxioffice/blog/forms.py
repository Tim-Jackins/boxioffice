from markdownx.fields import MarkdownxFormField
from django import forms

class NewPostForm(forms.Form):
    title = forms.CharField(required=True, max_length=20)
    text = MarkdownxFormField()
