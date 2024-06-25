from django.urls import path
from .views import (IndexView,UserRegisterView, student_login, ProfileView, add_book, edit_profile, view_books,
                    book_detail, CreateBookRequestView,RequestBooksView,AcceptBookRequestView,AcceptedBooksView)

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('login/', student_login, name='student_login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('add_book/', add_book, name='add_book'),
    path('view-books/', view_books, name='view_books'),  # Corrected view_books
    path('book/<int:pk>/', book_detail, name='book_detail'),  # Corrected book_detail
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('request/<int:pk>/', CreateBookRequestView.as_view(), name='create_request'),
    path('requested-books/', RequestBooksView.as_view(), name='requested_books'),
    path('libapp/accept/<int:pk>/', AcceptBookRequestView.as_view(), name='accept_book_request'),
    path('accepted-books/', AcceptedBooksView.as_view(), name='accepted_books'),



]





