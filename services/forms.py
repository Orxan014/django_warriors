from django import forms
from .models import Gigs, Comment
from captcha.fields import ReCaptchaField


class GigsForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Gigs
        fields = [
            'title',
            'content',
            'image',
            'tags',
        ]


class CommentForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Comment
        fields = [
            'name',
            'content',
        ]