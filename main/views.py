from django.shortcuts import render, redirect
from .models import ContactMessage

def index(request):
    if request.method == 'POST':
        ContactMessage.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        return redirect('thank_you')

    return render(request, 'main/index.html')

def thank_you(request):
    return render(request, 'main/thank_you.html')
