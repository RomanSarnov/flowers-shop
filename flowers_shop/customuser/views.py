from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout


class UserCreateView(View):
    def get(self, request):
        form = UserRegisterForm()
        context = {'form': form}
        template = "customuser/register.html"
        return render(request, template, context=context)

    def post(self, request):
        form = UserRegisterForm(request.POST)
        template = "customuser/register.html"
        context = {'form': form}
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, template, context=context)


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        template = 'customuser/login.html'
        context = {'form': form}
        return render(request, template, context=context)

    def post(self, request):
        form = UserLoginForm(data=request.POST)
        template = 'customuser/login.html'
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('shop')
        else:
            context = {'form': form}
            return render(request, template, context=context)

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('shop')