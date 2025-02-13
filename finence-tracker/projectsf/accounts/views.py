from django.http import JsonResponse
from django.shortcuts import render
from .forms import SignUpForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'User registered successfully!'}, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return render(request, 'register/sing-up.html')  # Asegúrate de que este archivo exista
