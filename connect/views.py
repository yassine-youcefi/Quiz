from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt,csrf_protect #Add this
from main.models import User
from django.shortcuts import get_list_or_404
# from .decorators import unauthenticated_user

@csrf_exempt
# @unauthenticated_user
def sign_up(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account is create successfuly for {username}')
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return redirect('main:index')
        else:
            groups = [{'name' : 'admin','index':0},{'name' : 'students  ','index':1}]    
            form = UserRegisterForm()
            users = User.objects.all()
            # for index, user in enumerate(users) :
            #     print('user ',user.filter(groups__name='admin'))
            #     if users.groups.all()[0] not in groups:
            #         groups.append({"name":users.groups.all()[0].name, "index":index})

            print('groups = ',groups)

            context = {
                    'form': form,
                    'groups' : groups
            }
        return render(request, 'sign_up.html', context=context)


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account was updated')
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'profile.html', context)
