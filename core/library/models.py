from django.db import models
# from account.models import  Author, Student, Staff
import account.models
# ----------------------------------------------------------------------------------
class Base(models.Model):
    """
    base information in tables
    """
    description = models.TextField(verbose_name='description', default= "default", blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated')

# ----------------------------------------------------------------------------------
class Category(Base):
    """
    books different category info
    """
    name = models.CharField(max_length=100, verbose_name='Name') #like adult child ...

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'category'

class Book(Base):
    """
    book's information
    """
    genre_choice = (
        ('Fiction', 'Fiction'),
        ('Science fiction', 'Science fiction'),
        ('Historical Fiction', 'Historical Fiction'),
        ('Romance novel', 'Romance novel'),
        ('Self-help book', 'Self-help book'),
        ('Horror fiction', 'Horror fiction'),
        ('History', 'History'),
        ('Fairy tale', 'Fairy tale'),
        ("Children's literature", "Children's literature"),
    )

    language_choice = (
        ('Persian', 'Persian'),
        ('French', 'French'),
        ('Italian', 'Italian'),
        ('German', 'German'),
        ('English', 'English'),
        ('Spanish', 'Spanish'),
    )

    author = models.ManyToManyField('account.Author', verbose_name='Author', related_name='books')
    category = models.ManyToManyField(Category, verbose_name='Category', related_name='books')
    # rate = models.ManyToManyField(User, related_name='', blank=True) rate books
# default=uuid.uuid4,
    isbn = models.UUIDField(unique=True, editable=False,  null=False, verbose_name='ISBN')  #UUID

    title = models.CharField(max_length=200, verbose_name='Title')
    genre = models.CharField(max_length=100, choices=genre_choice, verbose_name='Genre')
    language = models.CharField(max_length=100,choices=language_choice, default='English', verbose_name='Language')

    # file will be saved to MEDIA_ROOT / uploads / year / month / day
    image = models.ImageField(upload_to='uploads/% Y/% m/% d/', verbose_name='Book image', null=True, blank=True)

    publication_year = models.CharField(max_length=9999, verbose_name='Publication year')
    price = models.DecimalField(max_digits=500, decimal_places=2, verbose_name='Price')

    # def rates_number(self):
    #     return self.rate.count()

    def price(self):
        return str(self.title) + ": $" + str(self.price)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        db_table = 'book'
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
class Publication(Base):
    """ 
    books Publication info
    """
    book_publication = models.OneToOneField(Book,on_delete=models.SET_NULL, verbose_name='Book title', related_name='publication',null=True)

    name = models.CharField(max_length=100, verbose_name='Name') #like Pearson,Thomson Reuters ,Penguin Random House ..

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'publication'
# ----------------------------------------------------------------------------------
class Borrower(Base):
    """ 
    Borrower info
    """
    name = models.OneToOneField('account.Student',on_delete=models.PROTECT, verbose_name='Username', related_name='borrower')

    return_date = models.DateTimeField(auto_now_add=True, verbose_name='Return')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        db_table = 'borrower'

    # func to calculate the days of borrowing
    def days_of_borrowing(self):
        pass

# ----------------------------------------------------------------------------------
class Payment(Base):
    """ 
    book price info
    """
    book = models.ManyToManyField(Book, related_name='payment', verbose_name='Book')
    student = models.ForeignKey('account.Student',on_delete=models.PROTECT, related_name='payment', verbose_name='Username')

    def __str__(self):
        return "{}  :  {}".format(self.user.username, self.book.title)

    # most sell func
    def most_sell(self):
        pass

    class Meta:
        ordering = ['-created_at']
        db_table = 'payment'