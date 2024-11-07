
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('installation/', include('myapp.urls')),
    path('', include('templating.urls'))
]
