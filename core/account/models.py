from django.db import models
# login ba token anjam bedim

from django.contrib.auth.models import AbstractUser,AbstractBaseUser
# from library.models import Book,Borrower
import library.models
# --------------------------------------------------------------------------

class CustomUser(AbstractBaseUser):
    """ 
    user information
    """
    username = models.CharField(max_length=200 , verbose_name="Username")
    password = models.CharField(max_length=500 , verbose_name="Password")
    last_login = models.DateTimeField(auto_now_add=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, verbose_name="Email")
    phone_number = models.CharField(unique=True, max_length=11, verbose_name="Phone number")
    national_code = models.CharField(max_length=10,blank=True,null = True, verbose_name="National code")
    birthdate = models.DateField(help_text = "user's birthdate", default="None")
    gender = models.CharField(max_length=50, blank=True, null= True,default="None")
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated')


    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = []

    backend = 'account.custom_backend.ModelBackend'

    class Meta:
        db_table = 'custom_user'
        ordering = ['-created_at']

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
# --------------------------------------------------------------------------
class Staff(CustomUser):
    """ 
    staff info
    """
    status_choice = (
        ('active', 'active'),
        ('deactive', 'deactive'),
    )

    name = models.OneToOneField(CustomUser,on_delete=models.SET_NULL, verbose_name='staff', related_name='account_Staff_name',null=True)
    status = models.CharField(max_length=100,choices=status_choice, default='active', verbose_name='status')

    # add per for status

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.status)

    class Meta:
        db_table = 'staff'
# --------------------------------------------------------------------------
class Student(CustomUser):
    """ 
    Student info
    """
    book = models.ForeignKey('library.Book',on_delete=models.SET_NULL, verbose_name='book', related_name='book',null=True)
    name = models.OneToOneField(CustomUser,on_delete=models.SET_NULL, verbose_name='student', related_name='user',null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'student'

# --------------------------------------------------------------------------
class Author(CustomUser):
    """ 
    Author info
    """
    name = models.OneToOneField(CustomUser,on_delete=models.SET_NULL, verbose_name='author', related_name='account_Author_name',null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'author'
