from django import forms
from django.contrib.auth.models import User





from django import forms
from django.contrib.auth.models import User
from .models import Student, Book




class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['phone_no', 'department', 'roll_number', 'registered_id', 'college_name']


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")




from django import forms

class StudentLoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())


from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_name', 'author', 'book_id', 'description', 'book_image']


from django import forms
from django.contrib.auth.models import User
from .models import Student

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class StudentEditForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['phone_no', 'department', 'roll_number', 'registered_id', 'college_name']
