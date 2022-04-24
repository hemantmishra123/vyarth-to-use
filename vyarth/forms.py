from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from myapp.models import SubmitWaste,CollectWaste, Search
import django.contrib.sites
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"

class SubmitWasteForm(forms.ModelForm):
    class Meta:
        
        model= SubmitWaste
        fields = ['contact','communityName','typeofwaste','quantityofwaste','email','address']

class CollectWasteForm(forms.ModelForm):

    class Meta:
        model= CollectWaste
        fields = ['email']

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'Enter Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist!")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password!")
            if not user.is_active:
                raise forms.ValidationError("This user is not active")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    password2 = forms.CharField(
        label='Password confirmation',
        help_text='Enter the same password as before, for verification.',
        widget=forms.PasswordInput(attrs={'placeholder': 'Re Enter Password'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', ]

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        if commit:
            user.save()
        return user

class SearchForm(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Location'}))

    class Meta:
        model = Search
        fields = ['address', ]

