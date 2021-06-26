from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserLoginForm, UserRegisterForm, UserChangeForm
from .models import User



@login_required
def dashboard(request):
    return render(request,'accounts/dashboard.html')



def user_register(request):
    if request.method == 'POST' :
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user( cd['email'], cd['password1'], cd['full_name'], cd['national_code'], cd['mobile'], cd['address'] )
            user.save()
            login(request, user)
            messages.success(request,'ثبت نام با موفقیت انجام شد','success')
            return redirect('accounts:dashboard')
    else :
        form = UserRegisterForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/register.html', context)



@login_required
def user_edit(request):
    myid = request.user.id
    me = get_object_or_404(User, id = myid)
    if request.method =='POST':
        form = UserChangeForm(request.POST, instance=me)
        if form.is_valid():
            form.save()
            messages.success(request,'ویرایش مشخصات با موفقیت انجام شد','success')
            return redirect('accounts:dashboard')
    else :
        form = UserChangeForm(instance=me)
    context = {
        'form' : form
    }
    return render (request, 'accounts/user_edit.html', context)



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



@login_required
def user_logout(request):
    logout(request)
    messages.success(request,'خروج با موفقیت انجام شد','success')
    return redirect('accounts:dashboard')

