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

def send_otp(request):
    totp = pyotp.TOTP(pyotp.random_base32(), interval=1000)
    OtpEmail.otp = totp.now()
    request.session['otp_secrete_key'] = totp.secret
    valid_date= datetime.now() + timedelta(minutes=10)
    request.session['otp_valid_date'] = str(valid_date)
    # print(f'Your OTP is {otp}')

def OtpEmail(request, myuser, email):
    mail_subject = f'Your OTP for login is {OtpEmail.otp}'
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
    html_content = render_to_string ('otp_email.html', {
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
        'protocol': 'https' if request.is_secure() else 'http',
        'otp':  OtpEmail.otp
    })
    plain_msg = strip_tags(html_content)
    email = EmailMultiAlternatives(mail_subject, plain_msg, from_email, to=[email])
    email.attach_alternative(html_content, "text/html")
    email.content_subtype = "html"
    email.send()


