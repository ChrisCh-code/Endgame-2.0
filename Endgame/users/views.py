from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm # custom form import
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    
    if request.method == 'POST':
        #form = UserCreationForm(request.POST) 
        form = UserRegisterForm(request.POST) # replacing UserCreationForm with our custom UserRegisterForm to include the email field
        if form.is_valid():
            form.save() # save user into database if user is valid 
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created! You are now able to login {}'.format(username))
            return redirect('login')
    else:
        #form = UserCreationForm()
        form = UserRegisterForm # replacing UserCreationForm with our custom UserRegisterForm
    
    return render(request,'users/register.html',{'form':form})
    
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
