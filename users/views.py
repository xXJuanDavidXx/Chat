from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from . import forms
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm

# Create your views here.

class register(CreateView):

    form_class = SignUpForm
    template_name = 'users/register.html'
    success_url = reverse_lazy("home")


    def get_context_data(self, **kwargs):
        """
logout        Agrega `current_page` al contexto para usar en las plantillas.
        """
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'signup'
        return context



    def form_valid(self, form):
        """
        Procesa una validación exitosa del formulario.

        Guarda el nuevo usuario, lo autentica y lo inicia sesión.
        """
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return response

