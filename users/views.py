from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView

from .forms import CustomUserCreationForm

class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class LogOutView(TemplateView):
    template_name = 'logout_redirect.html'
    