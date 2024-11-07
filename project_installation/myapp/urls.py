from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about-us/', views.about_us, name='about' ),
    path('contact-us/', views.contact_us, name='contacts'),
    path('members/', views.members, name='members'),
    path('story/', views.our_story, name='our-story')
]
