from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic.edit import FormView


class RegisterFormView(FormView):
    form_class = UserCreationForm

    success_url = "/users/login/"

    template_name = "register.html"

    def form_valid(self, form):
        form.save()

        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "login.html"

    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")
