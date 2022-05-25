from django.db import models
from rest_framework import serializers

# Create your models here.

class Uploade(models.Model):
    BookName = models.CharField(max_length=100)
    prize = models.IntegerField()
    pages = models.IntegerField(default=None)


class BookSerializer(serializers.Serializer):
    BookName = serializers.CharField(max_length=100)
    prize = serializers.IntegerField()
    pages = serializers.IntegerField(default=None)

