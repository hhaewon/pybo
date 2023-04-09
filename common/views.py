from django.contrib.auth import authenticate, login
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View

from .forms import UserForm


class SignUpView(View):
    template_name = "common/signup.html"

    def post(self, request: HttpRequest):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("index")
        else:
            form = UserForm()
            context = {"form": form}
            return render(
                request=request, template_name=self.template_name, context=context
            )

    def get(self, request: HttpRequest):
        form = UserForm()
        context = {"form": form}
        return render(
            request=request, template_name=self.template_name, context=context
        )
