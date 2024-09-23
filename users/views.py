from typing import Any
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.views import View
from django.views.generic.base import TemplateView
from users.models import Users
from django.contrib.auth.hashers import check_password

from users.forms import AddSiteForm, UpdateDataForm, UserLoginForm, UserRegistrationForm

from django.contrib.auth import get_user_model

from vpn.models import UserSite

Users = get_user_model()


class UserView(TemplateView):
    template_name = 'users/profile.html'
    
    def get_context_data(self, **kwargs) -> dict:
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        
        # Add user and user_sites to the context    
        context["user"] = self.request.user
        context["title"] = "Профиль"
        
        # Fetch user's sites
        context["user_sites"] = UserSite.objects.filter(user=self.request.user)
        
        return context


class LoginView(View):

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = Users.objects.get(email=email)
            if user.check_password(password):
                authenticated_user = authenticate(request, email=email)
                if authenticated_user is not None:
                    login(request, authenticated_user)
                    return redirect('users:main')
                else:
                    print("Authentication failed")
        else:
            print(f"Form errors: {form.errors}")
        return render(request, self.template_name, {'form': form})


class RegistrationView(View):

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('users:main')
        else:
            print(form.errors)  
            
            
class UpdateDataView(View):

    def post(self, request):
        form = UpdateDataForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            if request.user.check_password(password):
                request.user.email = email
                request.user.save()
            
            return redirect('users:main')
        else:
            print(form.errors)  
            
            
class AddSiteView(View):

    def post(self, request):
        form = AddSiteForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name_site')
            url = form.cleaned_data.get('url_site')
            site = UserSite(user=request.user,name=name, url=url)
            site.save()
            
            return redirect('users:main')
        else:
            print(form.errors)  
            