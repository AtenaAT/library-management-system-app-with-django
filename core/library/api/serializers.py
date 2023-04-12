from rest_framework import serializers
from library.models import Book, Category, Payment,Publication, Borrower
# ---------------------------------------------
# ---------------------------------------------

# FIELDS = ()

# ---------------------------------------------
# ---------------------------------------------
class Category_Serializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# ---------------------------------------------
class Book_Serializer (serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

# ---------------------------------------------
class Publication_Serializer (serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'

# ---------------------------------------------
class Borrower_Serializer (serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = '__all__'

# ---------------------------------------------
class Payment_Serializer (serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

# ---------------------------------------------