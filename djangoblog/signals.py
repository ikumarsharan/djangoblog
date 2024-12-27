from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post
from django.contrib.auth.models import User
# from django.core.mail import EmailMessage
from sharanblog.settings import DEFAULT_FROM_EMAIL
# from sharanblog import settings

@receiver(post_save, sender=Post)
def SendEmail(sender , instance, created, **kwargs):
    if created:
        email = list(User.objects.values('email'))
        recepients = []
        for i in range(0, len(email)):
            recepients.append(email[i]['email'])
            pass
        email.send('New post on blog', str(instance.title), DEFAULT_FROM_EMAIL, recepients, fail_silently=False)
        pass


# def welcomeEmail(request, myuser, email):
#     mail_subject = 'Welcome to the site'
#     from_email = settings.DEFAULT_FROM_EMAIL
#     message = render_to_string('welcome_template.html', {
#         'fname': myuser.first_name,
#         'lname': myuser.last_name,
#         'domain': get_current_site(request).domain,
#         'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
#         'protocol': 'https' if request.is_secure() else 'http'
#     })
#     email = EmailMessage(mail_subject, message, from_email, to=[email])
#     email.send()