from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserRegisterForm , UserAdminChangeForm
from .models import User
from django.contrib.auth.models import Group


class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserRegisterForm
    list_display = ('full_name', 'email','is_admin', 'access_level', 'is_active')
    list_filter = ('is_admin', 'access_level')
    fieldsets = (
        (None,{'fields':('full_name','national_code')}),
        ('اطلاعات ورود',{'fields':('email','password')}),
        ('اطلاعات تماس',{'fields':('mobile','address')}),
        ('مجوزها',{'fields':('is_admin','access_level','is_active')})
    )
    add_fieldsets = (
        (None,{'fields':('full_name','national_code')}),
        ('اطلاعات ورود',{'fields':('email','password1','password2')}),
        ('اطلاعات تماس',{'fields':('mobile','address')}),
    )
    search_fields = ('email','national_code')
    ordering = ('is_admin','access_level','-id')
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)





