from django.shortcuts import render

def home(request):

    return render(request, 'myapp/index.html', context={})

def about_us(request):

    return render(request, 'myapp/about_us.html', context={})

def our_story(request):

    return render(request, 'myapp/story.html', context={})

def contact_us(request):

    return render(request, 'myapp/members.html', context={})

def members(request):

    return render(request, 'myapp/members.html', context={})