from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField


# Validation #


def validation_national_code (val) :
    if len(val) !=10 :
        return False
    else:
        try:
            int(val)
            return val
        except ValueError:
            return False


def validation_mobile (val) :
    if len(val) !=11 :
        return False
    elif val[:2] != '09':
        return False
    else:
        try:
            int(val)
            return val
        except ValueError:
            return False


def validation_phone (val):
    try:
        int(val)
        return val
    except ValueError:
        return False


# End Validation #


class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        label = 'رمز عبور' , 
        widget = forms.PasswordInput(attrs={
            'class' :'form-control'
        })
    )
    password2 = forms.CharField(
        label = 'تکرار رمز عبور' , 
        widget = forms.PasswordInput(attrs={
            'class' :'form-control'
        })
    )
    class Meta :
        model = User
        fields = ('email', 'full_name', 'national_code', 'date_birth', 'mobile', 'phone', 'address')
        widgets = {
            'email':forms.TextInput(attrs={
                'class' :'form-control' 
            }),
            'full_name':forms.TextInput(attrs={
                'class' :'form-control' 
            }),
            'national_code':forms.TextInput(attrs={
                'class' :'form-control' 
            }),
            'date_birth':forms.TextInput(attrs={
                'class' :'form-control' 
            }),
            'mobile':forms.TextInput(attrs={
                'placeholder' : '09...' ,
                'class' :'form-control' 
            }), 
            'phone':forms.TextInput(attrs={
                'class' :'form-control' 
            }),
            'address':forms.TextInput(attrs={
                'class' :'form-control' 
            }),
        }
        labels = {
            'email' : 'ایمیل',
            'full_name' : 'نام و نام خانوادگی',
            'national_code' : 'کدملی',
            'date_birth' : 'تاریخ تولد',
            'mobile' : 'شماره همراه',
            'phone' : 'شماره ثابت',
            'address' : 'آدرس',
        }
        error_messages = {
            ''
        }


    def clean_password2(self):
        p1 = self.cleaned_data['password1']
        p2 = self.cleaned_data['password2']
        if p1 and p2 and p1 != p2 :
            raise forms.ValidationError('رمزهای عبور همخوانی ندارند')
        return p2


    def clean_national_code(self):
        n = self.cleaned_data['national_code']
        result = validation_national_code(n)
        if result :
            return n
        else :
            raise forms.ValidationError('کدملی باید عدد 10 رقمی باشد')


    def clean_mobile(self):
        m = self.cleaned_data['mobile']
        result = validation_mobile(m)
        if result :
            return m
        else :
            raise forms.ValidationError('شماره همراه صحیح نمی باشد')


    def clean_phone(self):
        p = self.cleaned_data['phone']
        if p is None :
            return None
        result = validation_phone(p)
        if result :
            return p
        else :
            raise forms.ValidationError('شماره تلفن ثابت صحیح نمی باشد')


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
