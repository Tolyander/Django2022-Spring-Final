from rest_framework import serializers
from .models import Book,Journal

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Book

        extra_kwargs = {
            'id': {'read_only':True},
        }
    
    # def create(self,validated_data):
    #     instance = Book.objects.create(**validated_data)
    #     return instance
    
    # def update(self,instance,validated_data):
    #     for key,value in validated_data.items():
    #         if hasattr(instance,key):
    #             setattr(instance,key,value)
    #     instance.save()


class JournalSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Journal

        extra_kwargs = {
            'id': {'read_only':True},
        }