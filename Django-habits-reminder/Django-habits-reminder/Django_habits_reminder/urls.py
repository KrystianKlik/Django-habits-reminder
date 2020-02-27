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
    path('', habits.index, name='home'),
    path('habits/', include('habits.urls')),
    path('admin/', admin.site.urls),
    path('register/', users.register, name='register'),    
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html') , name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html') , name='logout'),
    path('home/', users.home, name='home'),
    #Password reset
    path('', include('django.contrib.auth.urls')),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"), name="password-reset"),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), name="password_reset_done"),
   
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),


    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
