"""
Definition of urls for Django_habits_reminder.
"""

from datetime import datetime
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

from django.conf import settings
from django.conf.urls.static import static

from users import views  as users
from habits import views as habits




urlpatterns = [
    path('', include('habits.urls')),
    path('admin/', admin.site.urls),
    path('register/', users.register, name='register'),    
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html') , name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html') , name='logout'),
    path('home/', users.home, name='home'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
