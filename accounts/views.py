from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from .models import CustomUser

class SignUpView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    model = CustomUSer
