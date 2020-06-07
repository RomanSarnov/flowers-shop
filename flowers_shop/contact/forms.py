from django import forms
from .models import Feedback, Newsletter


class FeedbackForm(forms.ModelForm):
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    copy = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = Feedback
        fields = ('subject', 'text', 'email', 'copy')


class NewsletterForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'nl-email', 'placeholder': 'Your E-mail'}))

    class Meta:
        model = Newsletter
        fields = ('email',)

    def clean_email(self):
        def clean_email(self):
            return self.cleanead_data['email'].lower()