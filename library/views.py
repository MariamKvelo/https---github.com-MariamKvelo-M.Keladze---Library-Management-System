from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('book_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    search_fields = ['title', 'authors__name', 'genre__name']
    filter_backends = [filter.SearchFilter]

from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count
from .models import Book, BookIssue

class PopularBooksAPIView(APIView):
    def get(self, request):
        books = Book.objects.annotate(issue_count=Count('bookissue')).order_by('-issue_count')[:10]
        data = [{'title': book.title, 'issue_count': book.issue_count} for book in books]
        return Response(data)
