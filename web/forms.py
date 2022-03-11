from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, widget=forms.EmailInput(
            attrs={
                # 'style': 'border-color: blue;',
                'placeholder': 'Email *',
                'class': 'form-control',
            }
        ))
    subject = forms.CharField(required=True, widget=forms.TextInput(
            attrs={
                # 'style': 'border-color: blue;',
                'placeholder': 'Subject *',
                'class': 'form-control',
            }
        ))
    message = forms.CharField(required=True, widget=forms.TextInput(
            attrs={
                # 'style': 'border-color: blue;',
                'placeholder': 'Your message *',
                'class': 'form-control',
            }
        ) )