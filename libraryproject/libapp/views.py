from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import login
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, StudentRegistrationForm, StudentLoginForm, BookForm
from .models import Student, Book,BookRequest
from django.views.generic import DetailView
from django.views import generic
from django.views import View
from django.views.generic import ListView, DetailView
from django.views import View
from django.shortcuts import render, get_object_or_404
from datetime import timedelta
from .models import Book
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from django.utils import timezone
from .models import BookRequest, AcceptedBookRequest

# Assuming you have a Book model









from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from .forms import UserRegisterForm, StudentRegistrationForm
from .models import Student



from django.shortcuts import render
from django.views import View

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

class UserRegisterView(View):
    template_name = 'registration/register.html'

    def get(self, request):
        user_form = UserRegisterForm()
        student_form = StudentRegistrationForm()
        return render(request, self.template_name, {
            'user_form': user_form,
            'student_form': student_form
        })

    def post(self, request):
        user_form = UserRegisterForm(request.POST)
        student_form = StudentRegistrationForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            student = student_form.save(commit=False)
            student.user = user
            student.save()

            login(request, user)
            return redirect(reverse_lazy('registration_success'))
        return render(request, self.template_name, {
            'user_form': user_form,
            'student_form': student_form
        })

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)


def student_login(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['user'] = user.pk
                return redirect('profile')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = StudentLoginForm()
    return render(request, 'student_login.html', {'form': form})


class ProfileView(DetailView):
    model = Student
    template_name = 'profile.html'
    context_object_name = 'student'

    def get_object(self):
        userid = self.request.session.get('user')
        return get_object_or_404(Student, user_id=userid)


@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_books')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})


def view_books(request):
    books = Book.objects.all()
    return render(request, 'view_books.html', {'books': books})



def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm, StudentEditForm

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        student_form = StudentEditForm(request.POST, instance=request.user.student)
        if user_form.is_valid() and student_form.is_valid():
            user_form.save()
            student_form.save()
            return redirect('profile')
    else:
        user_form = UserEditForm(instance=request.user)
        student_form = StudentEditForm(instance=request.user.student)
    return render(request, 'edit_profile.html', {
        'user_form': user_form,
        'student_form': student_form
    })


from django.views import View, generic
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book, BookRequest, Student
from django.contrib.auth.models import User

class CreateBookRequestView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        user = request.user  # Get the current logged-in User instance

        user_details = get_object_or_404(Student, user=user)  # Get the Student instance if needed

        if BookRequest.objects.filter(user=user, book=book).exists():
            return HttpResponse('You have already requested this book')
        else:
            BookRequest.objects.create(user=user, book=book)
            return HttpResponse('Your request has been sent')

class RequestBooksView(generic.ListView):
    model = BookRequest
    template_name = 'requested_books.html'
    context_object_name = 'requested_books'

    def get_queryset(self):
        user = self.request.user
        return BookRequest.objects.filter(user=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the book request objects along with their primary keys (pks) to the template
        context['book_requests'] = BookRequest.objects.filter(user=self.request.user)
        return context


from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.utils import timezone
from datetime import timedelta
from .models import BookRequest, AcceptedBookRequest

class AcceptBookRequestView(View):

    def get(self, request, pk):
        book_request = get_object_or_404(BookRequest, pk=pk)
        accepted_date = timezone.now()
        return_date = accepted_date + timedelta(days=5)  # Calculate return date

        # Calculate fine if book is returned late
        current_date = timezone.now()
        fine = 0
        if current_date > return_date:
            days_late = (current_date - return_date).days
            fine = days_late * 10

        # Create AcceptedBookRequest instance with calculated details
        accepted_book = AcceptedBookRequest.objects.create(
            details=book_request,
            accepted_date=accepted_date,
            return_date=return_date,  # Set the return_date
            fine=fine
        )

        # Delete the original book request
        book_request.delete()

        return redirect('requested_books')

    def post(self, request, pk):
        return self.get(request, pk)








from django.shortcuts import render
from django.views import View
from .models import AcceptedBookRequest

class AcceptedBooksView(View):
    def get(self, request):
        accepted_books = AcceptedBookRequest.objects.all()
        return render(request, 'accepted_books.html', {'accepted_books': accepted_books})



