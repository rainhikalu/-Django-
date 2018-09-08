from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path(r'borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'), #Added for challenge
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail')
]

urlpatterns += [
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]