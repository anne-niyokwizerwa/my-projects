from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from .models import *
from django import forms
from .models import News, Article, Contact

User = get_user_model()

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )


class SignUpForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}),

       }
class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=255)
class PasswordResetForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=255)

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title','summary', 'content', 'image', 'url']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Summary'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content'}),
            # 'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Image'}),
            'url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'URL'}),
        }

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author'}),
            # 'published_at': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Published At'}),
        }
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
