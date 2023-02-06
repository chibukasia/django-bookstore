from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from models import Book, Author
from serializers import AuthorSerializer, BookSerializer

# Create your views here.
class AuthorList(APIView):
    def get(self, request, format=None):
        authors = Author.objects.all()
        serializers = AuthorSerializer(authors, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

class AuthorDetails(APIView):
    def get_author(self, pk):
        try: 
            author = Author.objects.get(pk=pk)
            return author
        except Author.DoesNotExist:
            raise Http404 

    def get(self, request, pk, format=None):
        author = self.get_author(pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK) 

    def patch(self, request, pk, format=None):
        author = self.get_author(pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        author = self.get_author(pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)