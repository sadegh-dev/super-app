from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserLoginForm, UserRegisterForm
from .models import User

def dashboard(request):
    return render(request,'accounts/dashboard.html')


def user_register(request):
    if request.method == 'POST' :
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user( cd['email'], cd['password1'], cd['full_name'], cd['national_code'], cd['date_birth'], cd['mobile'], cd['address'] )
            user.save()
            #login(request, user)
            messages.success(request,'ثبت نام با موفقیت انجام شد','success')
            return redirect('accounts:dashboard')
    else :
        form = UserRegisterForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/register.html', context)


def user_login(request):
    next = request.GET.get('next')
    if request.method == 'POST' :
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None :
                login(request, user)
                messages.success(request,'ورود با موفقیت انجام شد','success')
                if next :
                    return redirect(next)
                return redirect('accounts:dashboard')
            else :
                messages.success(request,'ایمیل یا رمز عبور صحیح نمی باشد','danger')
    else :
        form = UserLoginForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)


def user_logout(request):
    logout(request)
    messages.success(request,'خروج با موفقیت انجام شد','success')
    return redirect('accounts:dashboard')


