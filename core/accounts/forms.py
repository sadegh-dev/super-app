from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label = 'رمز عبور' , 
        widget = forms.PasswordInput
    )
    password2 = forms.CharField(
        label = 'تکرار رمز عبور' , 
        widget = forms.PasswordInput
    )
    class Meta :
        model = User
        fields = ('email', 'full_name', 'national_code', 'date_birth', 'mobile', 'phone', 'address')

    def clean_password2(self):
        p1 = self.cleaned_data['password1']
        p2 = self.cleaned_data['password2']
        if p1 and p2 and p1 != p2 :
            raise forms.ValidationError('رمزهای عبور همخوانی ندارند')
        return p2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit :
            user.save()
        return user

class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta :
        model = User
        fields = ('email', 'full_name', 'national_code', 'date_birth', 'mobile', 'phone', 'address')
    
    def clean_password(self):
        return self.initial['password']


class UserLoginForm(forms.Form):
    email = forms.CharField(
        max_length=100 ,
        widget= forms.EmailInput(attrs={
            'class':'form-control'
        }))
    password = forms.CharField(
        max_length=100 ,
        widget= forms.PasswordInput(attrs={
            'class':'form-control'
        }))


