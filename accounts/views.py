from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import UserRegistrationForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"{username}, your account has been created!"
            )
            return redirect("login")
        else:
            form = UserRegistrationForm()
            return render(request, "accounts/register.html", {"form": form})
