from django import forms
from .models import Message
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm


class LoginForm(forms.Form):
    username = forms.CharField(label='',  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = '', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].help_text = '<small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small>'
        self.fields['username'].label = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<small><ul><li>Your password can’t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul></small>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Verify Password'
        self.fields['password2'].help_text = ''
        self.fields['password2'].help_text = '<small><ul><li>Enter the same password as before, for verification.</li></ul></small>'

class ProfileForm(forms.ModelForm):
    username = forms.CharField(label='', help_text='<small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small>', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username'}))
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'message')

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)


        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Name'
        self.fields['name'].label = ''

        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = 'Message'
        self.fields['message'].label = ''

class PasswordChange(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password1 = forms.CharField(widget=forms.PasswordInput)
    new_password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
    def __init__(self, *args, **kwargs):
        super(PasswordChange, self).__init__(*args, **kwargs)


        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['old_password'].widget.attrs['placeholder'] = 'Old Password'
        self.fields['old_password'].label = ''

        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'New Password'
        self.fields['new_password1'].label = ''
        
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Verify New Password '
        self.fields['new_password2'].label = ''
