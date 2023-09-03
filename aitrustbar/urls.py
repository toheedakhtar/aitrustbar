"""aitrustbar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from users import views as users_views

# app_name = 'users'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('poll.urls')),

    # path('users/', include('users.urls')),
    path('signup/', users_views.signup , name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html') , name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html") , name='logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='users/resetPassword.html') , name='reset_password'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/resetPassword_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name= 'users/resetPass-form.html') , name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/resetPass-complete.html') , name='password_reset_complete'),


]
