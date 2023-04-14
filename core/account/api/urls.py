from django.urls import path
# orgnize here!
from .views import Staff_Create_APIView,Staff_List_APIView,Staff_Update_Delete_APIView,Student_Create_APIView,Student_List_APIView,Student_Update_Delete_APIView,Author_Create_APIView,Author_List_APIView,Author_Update_Delete_APIView

app_name = 'api'

urlpatterns = [

    path('registration/', .as_view(), name='registration'),








# modify names

    # -- staff
    # -------------------------- List ---------------------------------------
    path('staff/list/', Staff_List_APIView.as_view(), name='staff list'),
    # -------------------------- Create ---------------------------------------
    path('staff/create/', Staff_Create_APIView.as_view(), name='create staff'),
    # -------------------------- Update Delete---------------------------------------
    path('staff/update-delete/<int:pk>/', Staff_Update_Delete_APIView.as_view(), name='update & delete staff'),

    
    # -- student
    # -------------------------- List ---------------------------------------
    path('student/list/', Student_List_APIView.as_view(), name='student list'),
    # -------------------------- Create ---------------------------------------
    path('student/create/', Student_Create_APIView.as_view(), name='create student'),
    # -------------------------- Update Delete---------------------------------------
    path('student/update-delete/<int:pk>/', Student_Update_Delete_APIView.as_view(), name='update & delete student'),


    # -- author
    # -------------------------- List ---------------------------------------
    path('author/list/', Author_List_APIView.as_view(), name='author list'),
    # -------------------------- Create ---------------------------------------
    path('author/create/', Author_Create_APIView.as_view(), name='create author'),
    # -------------------------- Update ---------------------------------------
    path('author/update-delete/<int:pk>/', Author_Update_Delete_APIView.as_view(), name='update & delete author'),

]
