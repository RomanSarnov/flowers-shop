from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordChangeForm
from .forms import CustomPasswordChangeForm, CustomSetPasswordForm, CustomResetPasswordForm


urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(form_class=CustomPasswordChangeForm), name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(form_class=CustomResetPasswordForm), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(form_class=CustomSetPasswordForm), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')


]