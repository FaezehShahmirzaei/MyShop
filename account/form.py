from django import forms
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField

from django.core.exceptions import ValidationError

from account.models import Account, MyAccountManager


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text="Required. Add a valid email address. ")
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ("email", "username")

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = MyAccountManager.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f'Email {email} is already in use.')

    def clean_username(self):
        username = self.cleaned_data['email'].lower()
        try:
            account = MyAccountManager.objects.get(email=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f'Email {username} is already in use.')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('password dont match')
        return cd['password2']

    def save(self, commit=True):
        Account = super().save(commit=False)
        Account.set_password(self.cleaned_data['password1'])
        if commit:
            Account.save()
        return Account


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text="you can change password  using <a href=\"../password/\" >this form</a>")

    class Meta:
        model: Account
        fields = ('profile_image', 'is_customer', 'is_active', 'username', 'last_login', 'password')


class UserRegistrationForm(forms.Form):
    email = forms.EmailField(max_length=60, help_text="Required. Add a valid email address. ")
    phone = forms.CharField(label='mobile', max_length=11, help_text='Required.Add a valid mobile.')
    username = forms.CharField(max_length=30, help_text='input a username less than 30 character.')
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data['email']
        print(email)
        user = Account.objects.filter(email=email).exists()
        if user:
            raise ValidationError('This email is already exists.')
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        user = Account.objects.filter(mobile_number=phone).exists()
        if user:
            raise ValidationError('This mobile is already exists.')
        return phone

    def clean_username(self):
        username = self.cleaned_data['username']
        user = Account.objects.filter(username=username).exists()
        if user:
            raise ValidationError('This username is already exists.')
        return username

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('password dont match')
        return cd['password2']


class VerifyCodeForm(forms.Form):
    code = forms.IntegerField()
