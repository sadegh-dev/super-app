from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .forms import UserLoginForm

def test(request):
    return render(request,'accounts/test.html')

def login(request):
    next = request.GET.get('next')
    if request.method == 'POST' :
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])

            if user is not None :
                auth_login(request, user)
                messages.success(request,'ورود با موفقیت انجام شد','success')
                if next :
                    return redirect(next)
                return redirect('accounts:test')
            else :
                messages.success(request,'ایمیل یا رمز عبور صحیح نمی باشد','danger')
    else :
        form = UserLoginForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)


