from .serializers import Staff_Serializer, Student_Serializer, Author_Serializer
from account.models import Staff,Student,Author
from rest_framework import generics

# -------------- Staff -------------------------------------
# ------------- Create ------------------------
class Staff_Create_APIView (generics.CreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = Staff_Serializer  


# ------------- List --------------------------
class Staff_List_APIView (generics.ListAPIView):
    queryset = Staff.objects.all()
    serializer_class = Staff_Serializer  


# ------------Update, Delete------------------
class Staff_Update_Delete_APIView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = Staff_Serializer



# -------------- Student ----------------------------------------------
# ------------- Create ------------------------
class Student_Create_APIView (generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = Student_Serializer 

# ------------- List --------------------------
class Student_List_APIView (generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = Student_Serializer  


# ------------Update, Delete------------------
class Student_Update_Delete_APIView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = Student_Serializer


# -------------- Author ----------------------------------------------
# ------------- Create ------------------------
class Author_Create_APIView (generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = Author_Serializer  


# ------------- List --------------------------
class Author_List_APIView (generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = Author_Serializer  


# ------------Update, Delete------------------
class Author_Update_Delete_APIView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = Author_Serializer

