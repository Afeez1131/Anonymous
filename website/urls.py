from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),

    # path('login/', views.login_user, name='login'),
    # path('logout/', views.logout_user, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='website/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='website/logout_success.html'), name='logout'),


    path('register/', views.register_user, name='register'),
    path('password_change/', views.change_password, name='password_change'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),

    path('home.html/', views.user_home, name='user_home'),
    path('message/<str:user>/', views.user_message, name='message'),

    path('delete_message/<int:id>/', views.delete_message, name='delete_message'),  
    path('spam_message/<int:id>/', views.spam_message, name='spam_message'),  


    # path('password_change', auth_views.PasswordChangeView.as_view(), name='password_change'),

    # path('password_reset')
]