from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(request):
    return render(request,'register.html')

def signup(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context={
        'form':form
    }
    return render(request,'signup.html',context)