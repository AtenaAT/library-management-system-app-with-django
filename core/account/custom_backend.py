from django.contrib.auth.backends import ModelBackend
from .models import CustomUser
from django.contrib.auth.hashers import check_password

class Custom_Backend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserInfo.objects.get(username=username)

            # check =check_password(password)
            if  user.check_password(password):
                return user
            return None

        except UserInfo.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            return None

    def get_user(self, user_id):
        try:
            user = UserInfo.objects.get(pk=user_id)
        except UserInfo.DoesNotExist:
            return None