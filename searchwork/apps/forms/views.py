# coding: utf-8
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.template.response import TemplateResponse
from django.conf import settings
from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.models import User
from django.utils.http import is_safe_url
from django.shortcuts import resolve_url
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import (REDIRECT_FIELD_NAME, login as auth_login,
    logout as auth_logout, get_user_model, update_session_auth_hash)
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm

from forms import Reg

def base_index(request):
	return render(request, "forms/base.html")


def my_log(request):
    form = Loguser(request.GET)
    if request.user.is_authenticated():
        return render(request, 'forms/welkom.html')
    else:
        form.Loguser()
    return render(request, 'forms/index.html', {'form':form})

def login(request):
    return render(request, 'forms/index.html')



def reg(request):
	if request.method == 'POST':
		form = Reg(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'forms/welkom.html')
	else:
		form = Reg()		
	return render(request, 'forms/register.html', {'form':form})


