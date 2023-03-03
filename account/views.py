import random

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .form import UserCreationForm, RegistrationForm, UserRegistrationForm, VerifyCodeForm, UserLoginForm
from django.views import View
from core.utils import send_otp_code
from django.contrib import messages
from .models import Account, OtpCode
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f'your are already authenticated as{user.email}')
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = kwargs.get("next")
            if destination:
                return redirect("index")
        else:
            context['registration_form'] = form
        return render(request, 'index', context)

    # def home(request):
    #     return render(request, 'home.html')


class UserRegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'account/register.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(1000, 9999)
            send_otp_code(form.cleaned_data['phone'], random_code)
            OtpCode.objects.create(phone_number=form.cleaned_data['phone'], code=random_code)
            request.session['user_registration_info'] = {
                'phone-number': form.cleaned_data['phone'],
                'email': form.cleaned_data['email'],
                'username': form.cleaned_data['username'],
                'raw-password': form.cleaned_data['password1'],
                'password': form.cleaned_data['password2'],
            }
            messages.success(request, 'we send you a code', 'success')
            return redirect('account:verify_code')
        return render(request, self.template_name, {'form': form})


class UserRegistrationVerifyCodeView(View):
    form_class = VerifyCodeForm

    def get(self, request):
        form = self.form_class
        return render(request, 'account/verify.html', {'form': form})

    def post(self, request):
        user_session = request.session['user_registration_info']
        code_instance = OtpCode.objects.get(phone_number=user_session['phone-number'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code:
                Account.objects.create_user(user_session['email'], user_session['username'], user_session['password'])
                code_instance.delete()
                messages.success(request, 'you are registered!', 'success')
                return redirect('core:home')
            else:
                messages.error(request, 'This code is note correct', 'danger')
                return redirect('account:verify_code')
        return redirect('core:home')


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'you logged out successfully', 'success')
        return redirect('core:home')


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'account/login.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,phone_number=cd['phoone'],password=cd['password'])
            if user is None:
                login(request,user)
                messages.success(request,'you loged in successfully','info')
                return redirect('home:home')
            messages.success(request,'phone por password is wrong ','warning')
        return render(request,self.template_name, {'form:form'})



def signin(request):
    return render(request, 'signin.html')


def index(request):
    return render(request, 'index.html')


def logout(request):
    return render(request, 'logout.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
