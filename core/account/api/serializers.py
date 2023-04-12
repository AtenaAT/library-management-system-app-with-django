from rest_framework import serializers
from account.models import Staff,Student,Author
# ---------------------------------------------
# ---------------------------------------------

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

