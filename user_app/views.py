# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from user_app.models import User
from user_app.forms import NewUserForm
# Create your views here.

def index(request):
    return render(request, 'user_app/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, 'user_app/users.html', context=user_dict)

def add_user(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return users(request)
        else:
            print('Eror Form Invalid')

    return render(request, 'user_app/create_form.html', {'form': form})
