from django.db import models


class FileFinder(models.Model):
    """
        FileFinder Model
    """
    title = models.CharField(max_length=100)
    item = models.FileField(upload_to='media/')


class Registration(models.Model):
    """
        Register Model
    """
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=12)


class User(models.Model):
    """
        User Model
    """
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=12)
