




from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Student(models.Model):
    DEPARTMENT_CHOICES = [
        ('CSE', 'Computer Science Engineering'),
        ('EC', 'Electronics and Communication'),
        ('EEE', 'Electrical and Electronics Engineering'),
        ('BCA', 'Bachelor of Computer Applications'),
        ('OTHER', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    phone_no = models.CharField(max_length=15)
    password = models.CharField(max_length=128)
    department = models.CharField(max_length=400, choices=DEPARTMENT_CHOICES)
    roll_number = models.CharField(max_length=10)
    registered_id = models.CharField(max_length=10)
    college_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.user.first_name} {self.user.last_name}"



class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    book_id = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    book_image = models.ImageField(upload_to='book_images/', null=True, blank=True)
    available_copies = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.book_name



class BookRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    request_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"Request by {self.user.username} for {self.book.book_name} on {self.request_date}"


class AcceptedBookRequest(models.Model):
    details = models.ForeignKey(BookRequest, on_delete=models.CASCADE, default=None)
    accepted_date = models.DateTimeField(auto_now_add=True)
    fine = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    return_date = models.DateTimeField()

    def __str__(self):
        return f"Accepted request for {self.details.book.book_name} by {self.details.user.username}"



