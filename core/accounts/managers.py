from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, password, full_name, national_code, mobile, address):
        if not email :
            raise ValueError('ایمیل الزامی است')
        if not full_name :
            raise ValueError('نام و نام خانوادگی الزامی است')
        if not national_code :
            raise ValueError('کدملی الزامی است')
        if not mobile :
            raise ValueError('موبایل الزامی است')
        if not address :
            raise ValueError('آدرس الزامی است')

        user = self.model(
            email = self.normalize_email(email) ,
            full_name = full_name ,
            national_code = national_code ,
            mobile = mobile ,
            address = address,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, full_name, national_code, mobile, address):
        user = self.create_user(email, password, full_name, national_code, mobile, address)
        user.is_admin = True
        user.save(using=self._db)
        return user





