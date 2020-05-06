from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    name = forms.CharField(label="Название товара")
    email = forms.EmailField(label="E-mail")
    subject = forms.CharField(label="Тема")
    message = forms.CharField(label="Сообщение",
                              widget=forms.widgets.Textarea)

    class Meta(object):
        model = Feedback
        fields = ('name', 'email', 'subject', 'message')
