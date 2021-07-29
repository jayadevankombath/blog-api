from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('api/',include('blog_api.urls',namespace='blogapi')),
    path('admin/', admin.site.urls),
    
]
