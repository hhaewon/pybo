from django.contrib.auth import authenticate, login
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View

from common.forms import UserForm


class SignUpView(View):
    def get(self, request: HttpRequest):
        form = UserForm()
        return render(request, "common/signup.html", {"form": form})

    def post(self, request: HttpRequest):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect("index")
        else:
            return render(request, "common/signup.html", {"form": form})
