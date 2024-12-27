from base64 import urlsafe_b64decode
from datetime import datetime, timedelta
from multiprocessing import AuthenticationError
from urllib.request import Request
from webbrowser import get
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import generic, View
#from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
#from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import RemoteUserBackend
from sharanblog import settings
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
# from .tokens import generate_token
from django_email_verification import send_email
from django.utils.html import strip_tags
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from .tokens import account_activation_token
from .utils import send_otp, OtpEmail
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.db.models.query_utils import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from members.forms import ProfileForm, form_validation_error, SetPasswordForm, PasswordResetForm # import the used form and related function to show errors
from members.models import Profile # import the Profile Model 
from django.contrib.auth.forms import AuthenticationForm
from django.template import RequestContext
from django.http.response import HttpResponseForbidden
from ipware import get_client_ip
import ipinfo
from django.core.mail import EmailMultiAlternatives
from sharanblog.settings import RECAPTCHA_KEY, RECAPTCHA_SECRET
from django_user_agents.utils import get_user_agent
import pyotp
from datetime import datetime, timedelta
from django.utils.datastructures import MultiValueDictKeyError


# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     template_name = 'registration/signup.html'
#     success_url = reverse_lazy('login')
def RegisterPage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
    
        if User.objects.filter(username=username):
            messages.error(request, "Username already exists!")
            return redirect('signup')
    
        if User.objects.filter(email=email):
            messages.error(request, "Email already exist")
            return redirect('signup')
    
        if len(username)>10 & len(username)<5:
            messages.error(request, "Username cannot be less than 5 character or greater than 10 character")
            return redirect('signup')
        if len(password1)<10:
            messages.error(request, "Password cannot be less than 12 character.")
            return redirect('signup')
        if not any(char.isdigit() for char in password1):
            messages.error(request, "Password should have at least one numeral.")
            return redirect('signup')
        if not any(char.isupper() for char in password1):
            messages.error(request, "Password should have at least one uppercase letter.")
            return redirect('signup')
        if not any(char.islower() for char in password1):
            messages.error(request, "Password should have at least one lower letter.")
            return redirect('signup')
        # if not any(char in isspecialsym() for char in password1):
        #     messages.error(request, "Password should have at least one special character.")
        #     return redirect('signup')
        if password1 != password2:
            messages.error(request, "Passwords didnot match")
            return redirect('signup')
        if not username.isalnum():
            messages.error(request, "Username must be alpha numeric")
            return redirect('signup')

        myuser = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password1)
        myuser.is_active = False
        myuser.save()
        activateEmail(request, myuser, email)
        # messages.success(request, 'Account is created successfully! Login to access' )
        return redirect('login')

    context = {}
    return render(request, 'registration/signup.html', context)

def LoginPage(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                # send_otp(request)
                request.session['username'] = username
                login(request, user)
                # messages.info(request, f"You are now logged in as {username}.")
                loginNotify(request, user, user.email)
                messages.success(request, f'An email with OTP has sent to your inbox.')
                # OtpEmail(request, user, user.email)
                # return redirect('EmailOtp.otp')
                return redirect('profile')   
        else:
            messages.error(request,"Invalid username or password")

    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={})

# def OtpView(request):
#     if request.method == "POST":
#         username = request.session['username']
#         otp_secrete_key = request.session['otp_secrete_key']
#         otp_valid_date = request.session['otp_valid_date']
#         OtpEmail.otp = request.POST.get('OtpEmail.otp', False)

#         if otp_secrete_key and otp_valid_date is not None:
#             valid_until = datetime.fromisoformat(otp_valid_date)
#             if valid_until > datetime.now():
#                 totp = pyotp.TOTP(otp_secrete_key, interval=1000)
#                 if totp.verify(OtpEmail.otp):
#                     user = get_object_or_404(User, username=username)
#                     login(request, user)
                    
#                     del request.session['otp_secrete_key']
#                     del request.session['otp_valid_date']
#                     return redirect('profile')
#                 else:
#                     messages.error(request, "Incorrect OTP, please verify and re-enter")
#             else:
#                 messages.error(request, "Oops! Something went wrong")
#         else:
#             messages.error(request, "Oops! Something went wrong")
                    
#     return render(request=request, template_name='registration/otp.html', context={})


def logout_request(request):
    logout(request)
    return redirect('login')


def activateEmail(request, myuser, email):
    mail_subject = 'Please confirm your email'
    from_email = settings.DEFAULT_FROM_EMAIL
    message = render_to_string('email_confirmation.html', {
        'fname': myuser.first_name,
        'lname': myuser.last_name,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
        'token': account_activation_token.make_token(myuser),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    # email = EmailMessage(mail_subject, message, from_email, to=[email])
    plain_msg = strip_tags(message)
    email = EmailMultiAlternatives(mail_subject, plain_msg, from_email, to=[email])
    email.attach_alternative(message, "text/html")
    email.content_subtype = "html"
    if email.send():
        messages.success(request, f'Thank you for signup! please check your inbox to confirm your email. Note: Check your spam folder.')
    else:
        messages.error(request, f'Problem sending confirmation email to {email}, check if you typed it correctly.')


def reactivateEmail(request, myuser, email):
    mail_subject = 'Please confirm your email.'
    from_email = settings.DEFAULT_FROM_EMAIL
    message = render_to_string('email_confirmation.html', {
        'fname': myuser.first_name,
        'lname': myuser.last_name,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
        'token': account_activation_token.make_token(myuser),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, from_email, to=[email])
    if email.send():
        messages.success(request, f'An mail sent with a new confirmation link, please check your inbox to confirm your email. Note: Check your spam folder.')
    else:
        messages.error(request, f'Problem sending confirmation email to {email}, check if you typed it correctly.')


# WElcome email
def welcomeEmail(request, myuser, email):
    mail_subject = 'Welcome to the site'
    from_email = settings.DEFAULT_FROM_EMAIL
    message = render_to_string('welcome_template.html', {
        'fname': myuser.first_name,
        'lname': myuser.last_name,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
        'token': account_activation_token.make_token(myuser),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    #email = EmailMessage(mail_subject, message, from_email, to=[email])
    plain_msg = strip_tags(message)
    email = EmailMultiAlternatives(mail_subject, plain_msg, from_email, to=[email])
    email.attach_alternative(message, "text/html")
    email.content_subtype = "html"
    email.send()
    #     messages.success(request, f'An mail sent with a new confirmation link, please check your inbox to confirm your email. Note: Check your spam folder.')
    # else:
    #     messages.error(request, f'Problem sending confirmation email to {email}, check if you typed it correctly.')


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and account_activation_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        welcomeEmail(request, myuser, myuser.email)
        messages.success(request, f'Thank you for email confirmation. Now you can login to your account.')
        return redirect('login')
    else:
        messages.error(request, f'Confirmation link is expired or invalid!')
    
    return redirect('login')

@method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileView(View):
    profile = None

    def dispatch(self, request, *args, **kwargs):
        self.profile, __ = Profile.objects.get_or_create(user=request.user)
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        context = {'profile': self.profile}
        return render(request, 'profile.html', context)

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES, instance=self.profile)
        # messages.success(request, 'Profile picture updated successfully!')

        if form.is_valid():
            profile = form.save()
            
            # to save user model info
            profile.user.first_name = form.cleaned_data.get('first_name')
            profile.user.last_name  = form.cleaned_data.get('last_name')
            profile.user.email      = form.cleaned_data.get('email')
            profile.user.birthday   = form.cleaned_data.get('birthday')
            # profile.user.city       = form.cleaned_data.get('city')
            profile.user.save()
            
            messages.success(request, 'Profile saved successfully')
        else:
            messages.error(request, form_validation_error(form))
        return redirect('profile')

# @login_required (login_url='login')
# def password_change(request):
#     user = request.user
#     if request.method == 'POST':
#         form = SetPasswordForm(user, request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Your password has been changed")
#             return redirect('login')
#         else:
#             for error in list(form.errors.values()):
#                 messages.error(request, error)

#     form = SetPasswordForm(user)
#     return render(request, 'password_reset_confirm.html', {'form': form})


def password_reset_request(request):
    form = PasswordResetForm()
    return render(
        request=request, 
        template_name="password_reset.html", 
        context={"form": form}
        )

def passwordResetConfirm(request, uidb64, token):
    return redirect("login")

def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            associated_user = get_user_model().objects.filter(Q(email=user_email)).first()
            if associated_user:
                subject = "Password reset request"
                message = render_to_string("template_reset_password.html", {
                    'user': associated_user,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
                    'token': account_activation_token.make_token(associated_user),
                    'userip': request.ipinfo.ip,
                    "protocol": 'https' if request.is_secure() else 'http'
                })
                plain_msg = strip_tags(message)
                email = EmailMultiAlternatives(subject, plain_msg, to=[associated_user.email])
                email.attach_alternative(message, "text/html")
                email.content_subtype = "html"
                if associated_user.is_active == False:
                        messages.error(request, "Account is not activated.")
                        reactivateEmail(request, associated_user, associated_user.email)
                        return redirect('login')
                if associated_user is None:
                    messages.error(request, "No account found with this email address")
                    return redirect('password_reset')
                if email.send():
                    if associated_user.is_authenticated: 
                        messages.success(request, """ An mail sent with instructions for setting your password, You should receive them shortly. If you don't receive an email, please make sure you've entered the address 
                                you registered with, and check your spam folder.
                            """
                        )
                        return redirect('profile')
                    else:
                        messages.success(request,""" An mail sent with instructions for setting your password, if an account exists with the email you entered. 
                                You should receive them shortly. If you don't receive an email, please make sure you've entered the address 
                                you registered with, and check your spam folder.
                            """
                        )
                        return redirect('login')
                else:
                    messages.error(request, "Problem sending reset password email, SERVER PROBLEM.")
                    return redirect('login')

            #return redirect('login')

        for key, error in list(form.errors.items()):
            if key == 'captcha' and error[0] == 'This field is required.':
                messages.error(request, "You must pass the reCAPTCHA test")
                continue

    form = PasswordResetForm()
    return render(
        request=request, 
        template_name="password_reset.html", 
        context={"form": form}
        )

def passwordResetConfirm(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been set. You may go ahead and log in now.")
                passwordChangeNotify(request, user, user.email)
                return redirect('login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

        form = SetPasswordForm(user)
        return render(request, 'password_reset_confirm.html', {'form': form})
    else:
        messages.error(request, "Password reset link is expired or invalid!")

    # messages.error(request, 'Something went wrong, redirecting back to Login page')
    return redirect("login")

# Password reset notification

def passwordChangeNotify(request, myuser, email):
    mail_subject = 'Password changed'
    from_email = settings.DEFAULT_FROM_EMAIL
    # message = render_to_string('template_password_notify.html', {
    #     'username': myuser.username,
    #     'fname': myuser.first_name,
    #     'lname': myuser.last_name,
    #     'userip': request.ipinfo.ip,
    #     'usercity': request.ipinfo.city,
    #     'usercountry': request.ipinfo.country,
    #     'useragent': get_user_agent(request),
    #     'domain': get_current_site(request).domain,
    #     'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
    #     'token': account_activation_token.make_token(myuser),
    #     'protocol': 'https' if request.is_secure() else 'http'
    # })
    # email = EmailMessage(mail_subject, message, from_email, to=[email])
    # email.send()
    html_content = render_to_string('template_password_notify.html', {
        'username': myuser.username,
        'fname': myuser.first_name,
        'lname': myuser.last_name,
        'userip': request.ipinfo.ip,
        # 'usercity': request.ipinfo.city,
        # 'userregion': request.ipinfo.region,
        # 'usercountry': request.ipinfo.country_name,
        'useragent': get_user_agent(request),
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
        'token': account_activation_token.make_token(myuser),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    plain_msg = strip_tags(html_content)
    email = EmailMultiAlternatives(mail_subject, plain_msg, from_email, to=[email])
    email.attach_alternative(html_content, "text/html")
    email.content_subtype = "html"
    email.send()
#Login Notify
def loginNotify(request, myuser, email):
    mail_subject = 'Successful sign-in to your account from new device'
    from_email = settings.DEFAULT_FROM_EMAIL
    # message = render_to_string('template_login_notify.html', {
    #     'username': myuser.username,
    #     'fname': myuser.first_name,
    #     'lname': myuser.last_name,
    #     'userip': request.ipinfo.ip,
    #     'usercity': request.ipinfo.city,
    #     'usercountry': request.ipinfo.country,
    #     'useragent': get_user_agent(request),
    #     'domain': get_current_site(request).domain,
    #     'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
    #     'token': account_activation_token.make_token(myuser),
    #     'protocol': 'https' if request.is_secure() else 'http'
    # })
    # plain_message=strip_tags(message)
    # email = EmailMessage(mail_subject, plain_message, from_email, to=[email])
    # email.send()
    html_content = render_to_string('template_login_notify.html', {
        'username': myuser.username,
        'fname': myuser.first_name,
        'lname': myuser.last_name,
        'userip': request.ipinfo.ip,
        # 'usercity': request.ipinfo.city,
        # 'userregion': request.ipinfo.region,
        # 'usercountry': request.ipinfo.country_name,
        'useragent': get_user_agent(request),
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
        'token': account_activation_token.make_token(myuser),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    plain_msg = strip_tags(html_content)
    email = EmailMultiAlternatives(mail_subject, plain_msg, from_email, to=[email])
    email.attach_alternative(html_content, "text/html")
    email.content_subtype = "html"
    email.send()

class GoogleRecaptchaMixin:
    def post(self, request, *args, **kwargs):
        g_recaptcha_response = request.POST.get('g-recaptcha-response', None)
        client_ip, is_routable = get_client_ip(request)
        response = request.post(
            "https://www.google.com/recaptcha/api/siteverify",
            data={
                "secret": RECAPTCHA_SECRET,
                "response": g_recaptcha_response,
                "remoteip": client_ip
            }
        )
        response_dict = response.json()
        if response_dict.get("success", None):
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseForbidden(*args, **kwargs)
        

#Forgot username request

def username_reset_request(request):
    form = PasswordResetForm()
    return render(
        request, 'username_request.html', 
        context_instance = RequestContext(request)
        )

def username_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            associated_user = get_user_model().objects.filter(Q(email=user_email)).first()
            if associated_user:
                subject = "Username request"
                message = render_to_string("username_request_template.html", {
                    'user': associated_user,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
                    'userip': get_client_ip(request),
                    "protocol": 'https' if request.is_secure() else 'http'
                })
                email = EmailMessage(subject, message, to=[associated_user.email])
                if associated_user.is_active == False:
                        messages.error(request, "Account is not activated. An mail sent to your register email address to reactivate your account.")
                        reactivateEmail(request, associated_user, associated_user.email)
                        return redirect('login')
                if associated_user is None:
                    messages.error(request, "No account found with this email address")
                    return redirect('username_reset')
                if email.send():
                    messages.success(request, """ An mail sent to retrieve your username, You should receive them shortly. If you don't receive an email, please make sure you've entered the address 
                                you registered with, and check your spam folder.
                            """
                        )
                    return redirect('login')
                else:
                    messages.error(request, "Problem sending reset password email, SERVER PROBLEM.")
                    return redirect('login')

            #return redirect('login')

#otp view

