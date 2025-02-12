from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Cambia por la vista adecuada después de registro
    else:
        form = SignUpForm()
    return render(request, 'accounts/sing_up.html', {'form': form})
