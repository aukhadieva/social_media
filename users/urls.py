from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import UserLoginView, UserRegisterView, UserProfileView, EmailVerificationView, UserResetPassword


app_name = UsersConfig.name

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('verify/<str:email>/<uuid:key>', EmailVerificationView.as_view(), name='verify'),
    path('reset_password', UserResetPassword.as_view(), name='reset_password')
]
