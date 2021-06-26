from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField


# ---- Validation -------------------- #

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


# ---- End Validation ---------------- #


class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta :
        model = User
        fields = ('email', 'full_name', 'national_code', 'mobile', 'address')
    
    def clean_password(self):
        return self.initial['password']



class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        max_length = '20',
        label = 'رمز عبور' , 
        widget = forms.PasswordInput(attrs={
            'class' :'form-control bg-light w-50'
        })
    )
    password2 = forms.CharField(
        max_length = '20',
        label = 'تکرار رمز عبور' , 
        widget = forms.PasswordInput(attrs={
            'class' :'form-control bg-light w-50'
        })
    )

    class Meta :
        model = User
        fields = ('email', 'full_name', 'national_code', 'mobile', 'address')
        widgets = {
            'email':forms.TextInput(attrs={
                'class' :'form-control bg-light w-50' ,
            }),
            'full_name':forms.TextInput(attrs={
                'class' :'form-control bg-light w-50' ,
            }),
            'national_code':forms.TextInput(attrs={
                'class' :'form-control bg-light w-50' ,
            }),
            'mobile':forms.TextInput(attrs={
                'placeholder' : '09...' ,
                'class' :'form-control bg-light w-50' ,
            }), 
            'address':forms.Textarea(attrs={
                'class' :'form-control bg-light w-50' ,
            }),
        }
        labels = {
            'email' : 'ایمیل',
            'full_name' : 'نام و نام خانوادگی',
            'national_code' : 'کدملی',
            'mobile' : 'شماره همراه',
            'address' : 'آدرس',
        }
        error_messages = {
            'email':{
                'unique':'کاربری با این ایمیل قبلا ثبت شده است',
                'invalid' : 'آدرس ایمیل صحیح نمی باشد' ,
            },
            'national_code' :{
                'unique':'کاربری با این کدملی قبلا ثبت شده است',
            },
            'mobile' :{
                'unique':'این شماره همراه قبلا ثبت شده است',
            }
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

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit :
            user.save()
        return user



class UserChangeForm(forms.ModelForm):
    class Meta :
        model = User
        fields = ('email', 'full_name', 'national_code', 'mobile', 'address')
        widgets = {
            'email':forms.TextInput(attrs={
                'class' :'form-control bg-light w-50' ,
            }),
            'full_name':forms.TextInput(attrs={
                'class' :'form-control bg-light w-50' ,
            }),
            'national_code':forms.TextInput(attrs={
                'class' :'form-control bg-light w-50' ,
            }),
            'mobile':forms.TextInput(attrs={
                'placeholder' : '09...' ,
                'class' :'form-control bg-light w-50' ,
            }), 
            'address':forms.Textarea(attrs={
                'class' :'form-control bg-light w-50' ,
            }),
        }
        labels = {
            'email' : 'ایمیل',
            'full_name' : 'نام و نام خانوادگی',
            'national_code' : 'کدملی',
            'mobile' : 'شماره همراه',
            'address' : 'آدرس',
        }
        error_messages = {
            'email':{
                'unique':'کاربری با این ایمیل قبلا ثبت شده است',
                'invalid' : 'آدرس ایمیل صحیح نمی باشد' ,
            },
            'national_code' :{
                'unique':'کاربری با این کدملی قبلا ثبت شده است',
            },
            'mobile' :{
                'unique':'این شماره همراه قبلا ثبت شده است',
            }
        }
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



class UserChangePassForm(forms.ModelForm):
    password1 = forms.CharField(
        label = 'رمز عبور',
        widget = forms.PasswordInput(attrs={
            'class' :'form-control bg-light w-50' ,
        })
    )
    password2 = forms.CharField(
        label = 'تکرار رمز عبور',
        widget = forms.PasswordInput(attrs={
            'class' :'form-control bg-light w-50' ,
        })
    )
    class Meta :
        model = User
        fields = ()

    def clean_password2(self):
        p1 = self.cleaned_data['password1']
        p2 = self.cleaned_data['password2']
        if p1 and p2 and p1 != p2 :
            raise forms.ValidationError(' رمز عبور هم خوانی ندارند ')
        return p1

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit :
            user.save()
        return user
        


class UserLoginForm(forms.Form):
    email = forms.CharField(
        max_length=254 ,
        required= True,
        label = 'ایمیل',
        widget= forms.EmailInput(attrs={
            'class':'form-control bg-light w-50',
            'placeholder' : 'your-email@email.com' ,
        }))
    password = forms.CharField(
        max_length=20 ,
        required= True,
        label = 'رمز عبور',
        widget= forms.PasswordInput(attrs={
            'class':'form-control bg-light w-50',
        }))



