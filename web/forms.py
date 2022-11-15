from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

# class ContactForm(forms.Form):
#     from_email = forms.EmailField(required=True, widget=forms.EmailInput(
#             attrs={
#                 # 'style': 'border-color: blue;',
#                 'placeholder': 'Email *',
#                 'class': 'form-control',
#             }
#         ))
#     subject = forms.CharField(required=True, widget=forms.TextInput(
#             attrs={
#                 # 'style': 'border-color: blue;',
#                 'placeholder': 'Subject *',
#                 'class': 'form-control',
#             }
#         ))
#     message = forms.CharField(required=True, widget=forms.TextInput(
#             attrs={
#                 # 'style': 'border-color: blue;',
#                 'placeholder': 'Your message *',
#                 'class': 'form-control',
#             }
#         ) )