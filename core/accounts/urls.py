from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('dashboard/',views.dashboard, name='dashboard'),

    # regiser - login - logout
    path('register/',views.user_register,name='register'),
    path('edit/',views.user_edit,name='user_edit'),
    path('change-password/',views.user_change_password,name='user_change_password'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # ......
]