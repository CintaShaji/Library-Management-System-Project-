
from django.contrib import admin
from .models import Student,Book,AcceptedBookRequest

# Register the Student model with the admin interface
admin.site.register(Student)
admin.site.register(Book)
admin.site.register(AcceptedBookRequest)

