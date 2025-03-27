from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from .forms import CustomUserCreationForm

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'front/login.html'
          
# view for user registration     
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
               # Save user but don't save the password yet
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])  # Hash the password
            user.save()
            login(request, user)    # Log in the user after successful registration, login function is used for session 
            # and another user cant login on the same server until one person is logged in on the same device
            return redirect('home')  # Redirect after successful registration
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': form}) 