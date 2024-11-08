from django.shortcuts import render

def home(request):

    return render(request, 'assignment/home.html', context={})

def about_us(request):

    return render(request, 'assignment/about.html', context={})

def our_story(request):

    return render(request, 'assignment/story.html', context={})

def contact_us(request):

    return render(request, 'assignment/contact.html', context={})

def members(request):

    return render(request, 'assignment/members.html', context={})