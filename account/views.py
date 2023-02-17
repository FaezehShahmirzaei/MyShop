from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

from .form import UserCreationForm, RegistrationForm


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
            email = form.cleandate.get('email').lower()
            raw_password = form.cleandate.get('password')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = kwargs.get("next")
            if destination:
                return redirect("index")
        else:
            context['registration_form'] = form
        return render(request, 'account/signin.html', context)

    # def home(request):
    #     return render(request, 'home.html')
