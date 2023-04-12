from django.urls import path
# orgnize here!
from .views import Category_Create_APIView,Category_List_APIView,Category_Update_Delete_APIView,Book_Create_APIView,Book_List_APIView,Book_Update_Delete_APIView,Publication_Create_APIView,Publication_List_APIView,Publication_Update_Delete_APIView,Borrower_Create_APIView,Borrower_List_APIView,Borrower_Update_Delete_APIView,Payment_Create_APIView,Payment_List_APIView,Payment_Update_Delete_APIView

urlpatterns = [

    # -- category
    # -------------------------- List ---------------------------------------
    path('category/list/', Category_List_APIView.as_view(), name='category list'),
    # -------------------------- Create ---------------------------------------
    path('category/create/', Category_Create_APIView.as_view(), name='create category'),
    # -------------------------- Update Delete---------------------------------------
    path('category/update-delete/<int:pk>/', Category_Update_Delete_APIView.as_view(), name='update & delete category'),

    
    # -- book
    # -------------------------- List ---------------------------------------
    path('book/list/', Book_List_APIView.as_view(), name='Book list'),
    # -------------------------- Create ---------------------------------------
    path('book/create/', Book_Create_APIView.as_view(), name='create Book'),
    # -------------------------- Update Delete---------------------------------------
    path('book/update-delete/<int:pk>/', Book_Update_Delete_APIView.as_view(), name='update & delete Book'),


    # -- publication
    # -------------------------- List ---------------------------------------
    path('publication/list/', Publication_List_APIView.as_view(), name='publication list'),
    # -------------------------- Create ---------------------------------------
    path('publication/create/', Publication_Create_APIView.as_view(), name='create publication'),
    # -------------------------- Update ---------------------------------------
    path('publication/update-delete/<int:pk>/', Publication_Update_Delete_APIView.as_view(), name='update & delete publication'),


    # -- borrower
    # -------------------------- List ---------------------------------------
    path('borrower/list/', Borrower_List_APIView.as_view(), name='borrower list'),
    # -------------------------- Create ---------------------------------------
    path('borrower/create/', Borrower_Create_APIView.as_view(), name='create borrower'),
    # -------------------------- Update Delete ---------------------------------------
    path('borrower/update-delete/<int:pk>/', Borrower_Update_Delete_APIView.as_view(), name='update & delete borrower'),


    # -- payment
    # -------------------------- List ---------------------------------------
    path('payment/list/', Payment_List_APIView.as_view(), name='payment list'),
    # -------------------------- Create ---------------------------------------
    path('payment/create/', Payment_Create_APIView.as_view(), name='create payment'),
    # -------------------------- Update Delete---------------------------------------
    path('payment/update-delete/<int:pk>/', Payment_Update_Delete_APIView.as_view(), name='update & delete payment'),



]
