from .serializers import Category_Serializer, Book_Serializer, Publication_Serializer, Borrower_Serializer, Payment_Serializer
from rest_framework import generics
from library.models import Book, Category,Payment,Borrower,Publication

# -------------- Category -------------------------------------
# ------------- Create ------------------------
class Category_Create_APIView (generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = Category_Serializer  


# ------------- List --------------------------
class Category_List_APIView (generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = Category_Serializer  


# ------------Update, Delete------------------
class Category_Update_Delete_APIView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = Category_Serializer



# -------------- Book ----------------------------------------------
# ------------- Create ------------------------
class Book_Create_APIView (generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = Book_Serializer 

# ------------- List --------------------------
class Book_List_APIView (generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = Book_Serializer  


# ------------Update, Delete------------------
class Book_Update_Delete_APIView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = Book_Serializer


# -------------- Publication ----------------------------------------------
# ------------- Create ------------------------
class Publication_Create_APIView (generics.CreateAPIView):
    queryset = Publication.objects.all()
    serializer_class = Publication_Serializer  


# ------------- List --------------------------
class Publication_List_APIView (generics.ListAPIView):
    queryset = Publication.objects.all()
    serializer_class = Publication_Serializer  


# ------------Update, Delete------------------
class Publication_Update_Delete_APIView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Publication.objects.all()
    serializer_class = Publication_Serializer


# -------------- Borrower ----------------------------------------------
# ------------- Create ------------------------
class Borrower_Create_APIView (generics.CreateAPIView):
    queryset = Borrower.objects.all()
    serializer_class = Borrower_Serializer  


# ------------- List --------------------------
class Borrower_List_APIView (generics.ListAPIView):
    queryset = Borrower.objects.all()
    serializer_class = Borrower_Serializer  


# ------------Update, Delete------------------
class Borrower_Update_Delete_APIView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Borrower.objects.all()
    serializer_class = Borrower_Serializer


# -------------- Payment ----------------------------------------------
# ------------- Create ------------------------
class Payment_Create_APIView (generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = Payment_Serializer  


# ------------- List --------------------------
class Payment_List_APIView (generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = Payment_Serializer  


# ------------Update, Delete------------------
class Payment_Update_Delete_APIView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = Payment_Serializer
