# from django.contrib.auth.tokens import PasswordResetTokenGenerator
# import six 

# class TokenGenerator(PasswordResetTokenGenerator):
#     def _make_hash_value(self, user, timestamp):
#         return (
#             six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active)
#         )

# generate_token = TokenGenerator()

from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six  

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, myuser, timestamp):
        return (
            six.text_type(myuser.pk) + six.text_type(timestamp)  + six.text_type(myuser.is_active)
        )

account_activation_token = AccountActivationTokenGenerator()