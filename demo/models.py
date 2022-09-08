from distutils.command.upload import upload
import email
from msilib.schema import Class
from pyexpat import model
from tkinter import CASCADE
from turtle import color
from urllib import request
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Size(models.TextChoices):
    SMALL = "small"
    MEDIUM = "medium"
    LARG = "larg"
class product(models.Model):
    name=models.CharField(max_length=20,unique=True)
    price=models.DecimalField(max_digits=5 ,decimal_places=2)
    img=models.ImageField(upload_to="media_imgs")
    size=models.CharField(max_length=10,choices=Size.choices,default="small")
    def __str__(self):
        return self.name+"/"+self.size
    def Is_huge(self):
        if self.size== "larg":
            return True
        return False
    Is_huge.boolean=True
class Dog(models.Model):
    name=models.CharField(max_length=100,default="boby",null=False)
    age=models.IntegerField()
    color=models.CharField(max_length=20)
    def __str__(self):
        return self.name
class courses(models.Model):
    name=models.CharField(max_length=100,default="boby",null=False)
    class Meta:  
        db_table = "courses"
    def __str__(self):
        return self.name
class student(models.Model):
    name=models.CharField(max_length=100,default="boby",null=False)
    email=models.EmailField(max_length=50,unique=True)
    courses=models.ManyToManyField(courses)
    class Meta:  
        db_table = "student"
    def __str__(self):
        return self.name
class Colour(models.TextChoices):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
class item(models.Model):
    name=models.CharField(max_length=100,default="boby",null=False)
    img=models.ImageField(upload_to="media_imgs")
    price=models.DecimalField(max_digits=5,decimal_places=2)
    flavor=models.CharField(max_length=100,default="red",choices=Colour.choices)
    class Meta:  
        db_table = "items"
    def __str__(self):
        return self.name
class comment(models.Model):
    title=models.CharField(max_length=10)
    body=models.TextField(max_length=50,default="body")
    product=models.ForeignKey(product ,on_delete=models.CASCADE) 
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    class Meta:
        db_table="comments"
    def __str__(self):
        return self.name
