from dataclasses import field, fields
from email.policy import default
from logging import PlaceHolder
from pyexpat import model
from tkinter import TRUE, Widget
from django import forms
from django.forms import TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . import models
class AddItemForm(forms.ModelForm):    
    # name = forms.CharField(max_length=100,required=TRUE,widget=forms.TextInput(attrs={'class': "form-control p-4",'placeholder':"name"}))
    # img = forms.ImageField(label='uploade image')
    # color = forms.ChoiceField(choices=models.Colour.choices)
    # price=forms.IntegerField(label="price",help_text="enter price")
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for key, field in self.fields.items():
    #         field.label = ""
    class Meta:
        model=models.item
        fields=("name","img","flavor","price")
        # fields='__all__'
class ProductForm(forms.ModelForm): 
    name=forms.CharField(  max_length=100,required=TRUE,widget=forms.TextInput(attrs={'class': "form-control p-4",'placeholder':"product_name"})) 
    img=forms.ImageField(label='',widget=forms.FileInput(attrs={"aria-describedby":"inputGroupFileAddon04"}))
    size=forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control "}),choices=models.Size.choices,)
    price=forms.DecimalField(widget=forms.TextInput(attrs={'class': "form-control "}))

    class Meta:
        model=models.product
        fields=("name","img","size","price")
        # fields='__all__'
        Widgets={
            'name':TextInput(attrs={'placeholder':'form-control p-4'}),
        }

class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1',"password2"]
        # fields='__all__'
class CommentForm(forms.ModelForm):
    title=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':"form-control p-4","placeholder":"title",}))
    body=forms.CharField(widget=forms.Textarea(attrs={'class':"form-control p-4","placeholder":"leave your comment","rows":4,"cols":8}))
    class Meta:
        model=models.comment
        # fields=[]
        fields='__all__'
