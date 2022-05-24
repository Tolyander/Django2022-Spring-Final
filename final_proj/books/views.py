from rest_framework import viewsets
from .models import Book,Journal
from .serializers import BookSerializer,JournalSerializer
from rest_framework import decorators
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class BookView(viewsets.ViewSet):


    def retrieve(self,request,pk):
        data = get_object_or_404(Book,pk=pk)
        serializer = BookSerializer(data)
        return Response(serializer.data)

    def list(self,request):
        data = Book.objects.all()
        serializer = BookSerializer(data,many=True)
        return Response(serializer.data)

    def update(self,request,pk):
        instance = get_object_or_404(Book,pk=pk)
        serializer = BookSerializer(instance=instance,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

    def create(self,request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def destroy(self,request,pk):
        instance = get_object_or_404(Book,pk=pk)
        instance.delete()
        return Response()

class JournalView(viewsets.ViewSet):


    def retrieve(self,request,pk):
        data = get_object_or_404(Journal,pk=pk)
        serializer = JournalSerializer(data)
        return Response(serializer.data)

    def list(self,request):
        data = Journal.objects.all()
        serializer = JournalSerializer(data,many=True)
        return Response(serializer.data)

    def update(self,request,pk):
        instance = get_object_or_404(Journal,pk=pk)
        serializer = JournalSerializer(instance=instance,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

    def create(self,request):
        serializer = JournalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def destroy(self,request,pk):
        instance = get_object_or_404(Journal,pk=pk)
        instance.delete()
        return Response()