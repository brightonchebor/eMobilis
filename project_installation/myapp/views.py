from django.shortcuts import render

def home(request):

    return render(request, 'myapp/index.html', context={})

def about_us(request):

    return render(request, 'myapp/about_us.html', context={})