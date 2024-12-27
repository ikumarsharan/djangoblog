from django.urls import path, include, re_path
from . import views
# from django.contrib.auth import views as auth_views
from django_email_verification import urls as mail_urls


urlpatterns = [
    path('signup/', views.RegisterPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    # path('otp/', views.OtpView, name='EmailOtp.otp'),
    path("logout/", views.logout_request, name= "logout"),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path("password-reset/", views.password_reset_request, name="password_reset"),
    path('password-reset/<uidb64>/<token>', views.passwordResetConfirm, name='password_reset_confirm'),
    path('myprofile/', views.ProfileView.as_view(), name='profile'),
    #path('send_email/', send_email),
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
    path("username-reset/", views.username_reset_request, name="username_reset"),
    path('email/', include(mail_urls)),
    
    #re_path(r'profile/(?P<username>[a-zA-Z0-9]+)$', views.get_user_profile),
]
