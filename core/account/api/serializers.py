from rest_framework import serializers
from account.models import Staff,Student,Author,CustomUser
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions


# ---------------------------------------------
# ---------------------------------------------

# -- login serializer
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
            raise serializers.ValidationError({'password': list(e.massages)})
        return super().validate(attrs)

    def create(self,validated_data):
        validated_data.pop('password1',None)

        return CustomUser.objects.create_user(**validated_data)

        # check the user model of course











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

