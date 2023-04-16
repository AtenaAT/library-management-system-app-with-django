from rest_framework import serializers
from account.models import Staff,Student,Author,CustomUser
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
# ---------------------------------------------
# ---------------------------------------------

# -- registration serializer
class Registration_Serializer(serializers.ModelSerializer):
    password_confrimation = serializers.CharField(max_length=300,write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email' , 'password','password_confrimation']

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password_confrimation'):
            raise serializers.ValidationError({'error':'password didnt match'})

        try:
            validate_password(attrs.get('password'))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'password': list(e.messages)})
        return super().validate(attrs)

    def create(self,validated_data):
        validated_data.pop('password_confrimation',None)

        return CustomUser.objects.create_user(**validated_data)

# check the user model of 


 
# -- login serializer
class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label=_("email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        username = attrs.get('email')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


# FIELDS = ()

# ---------------------------------------------
# ---------------------------------------------
class Staff_Serializer (serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

# ---------------------------------------------
class Student_Serializer (serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

# ---------------------------------------------
class Author_Serializer (serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

