from .serializers import Staff_Serializer, Student_Serializer, Author_Serializer
from account.models import Staff,Student,Author
from rest_framework import generics
from .serializers import Registration_Serializer,CustomAuthTokenSerializer
from rest_framework.response import Response
from rest_framework import status

# modify class names
# --- registration ---
class Registration_APIView(generics.GenericAPIView):
    serializer_class = Registration_Serializer

    # make obj
    def post(self, request, *args, **kwargs):
        # serializer = self.serializer_class
        serializer = Registration_Serializer(data= request.data)

        if serializer.is_valid():
            serializer.save()
            data = { 'email': serializer.validated_data['email']}

            return Response(data, status= status.HTTP_201_CREATED)  
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

 

# -- login
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })








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

