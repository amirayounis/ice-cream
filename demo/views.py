from contextvars import Context
from email.mime import image
from multiprocessing import context
from unicodedata import name
from xml.dom.minidom import Comment
from django.shortcuts import render ,redirect
from django.http import HttpResponse,HttpResponseRedirect
from demo import models
from .forms import AddItemForm,ProductForm,UserForm,CommentForm
from demo.models import item,comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate ,login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages #import messages


# Create your views here.
def index(request):
    res=HttpResponse("<h1>hello Django !!!</h1>")
    res.write("<p>firstapp<p>")
    name=request.GET
    for item in name:
        res.write(item+":"+name[item]+"<br>")
    res.write(request.__dir__)
    # res['content-type']="text/HTML"
    return res
    
def post(request,x):
#    y=request.__dir__
   res=HttpResponse("<h1>post detailes !!!</h1>"+str(x))
#    res.write()
   return res

def posts(request):
    
     return render(request,"products.html",{"items":item.objects.all()})
def addd(request):
    
     return render(request,"products.html",{"items":item.objects.all()})

def add(request):
     form=AddItemForm()
     if request.method == "POST":
        form=AddItemForm(request.POST)
        # if form.is_valid():
        AddItemForm.save()
            # print(request.POST['name']) 
            # pc = item(
            #     name = request.POST['name'],
            #     price = request.POST['price'],
            #     img = request.FILES['img'],
            #     flavor =request.POST['color'],
            # )
             
            # pc.save()
        
            # return redirect("posts")
        return render(request,"add_item.html",{"form":form})
def addd(request):
    
    error = {} 
    form = AddItemForm(request.POST)
    if request.POST:
        if form.is_valid():
            try:
                form.save()  
                return redirect('posts')  
            except:  
                pass
        

    return render(request,'add_item.html',{"form":form})



def products(request):
    items=models.product.objects.all()
    return render(request,"galary.html",{"items":items})
@login_required(login_url="/home/login")
def product(request,p_id):
    item=models.product.objects.get(id=p_id)
    form=CommentForm()
    if request.method =="POST":
       
        # form.product=item
        # form.user=request.user
        data={
            "title":request.POST['title'],
            "body":request.POST['body'],
            "product":item,
            "user":request.user}
        form=CommentForm(data)
        if form.is_valid():
             form.save()
    list=models.comment.objects.filter(product=item) 
    context={"item":item,
    "form":form,
    "list":list}
    return render(request,"detail.html",context)

def add_product(request):
    form=ProductForm()
    if request.method=="POST":
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid() :
            form.save()
            return redirect("products")    
        # # add product in database
        # # 1-creat instance product
        # p=models.product(name=request.POST['name']
        # ,price=request.POST['price']
        # ,size=request.POST['size']
        # ,img=request.FILES['img'])
        # # 2-save the instance
        # p.save()
        
    return render(request,"add_product.html",{"product_form":form})

def del_product(request,p_id):
   
    item=models.product.objects.get(id=p_id)
    item.delete()
    return redirect("products")
def product_edit(request,p_id):
    item=models.product.objects.get(id=p_id)
    form=ProductForm(instance=item)
    if request.method =="POST":
        form=ProductForm(request.POST,request.FILES,instance=item)
        if form.is_valid():    
           form.save()
           return redirect("products")
        # item.name=request.POST['name']
        # item.price=request.POST['price']
        # item.size=request.POST['size']
        # item.img=request.FILES['img']
        # item.update(name="ahmed")
        
    return render(request,"editform.html",{"form":form})

  


def del_comment(request,c_id):
    item=comment.objects.get(id=c_id)
    id=item.product.id
    item.delete()
    return redirect("product_details",p_id=id )
def register(request):
    form=UserForm()
    if request.method =="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            #authenticate new user
            user_name=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user=authenticate(username=user_name, password=password)
            login(request,user)
            return redirect("products")


    context={
        "form":form

    }
    return render(request,"register.html",context)
def login_user(request):
    if request.method =="POST":
        form=UserForm(request.POST)
        
            #authenticate new user
        user_name=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=user_name, password=password)
        if user is not None :
            login(request,user)
            request.session['fav'] = 0 
            request.session['conter']=0
            return redirect("products")
        else:
            messages.error(request,"the username or password did not match")
    return render(request,"login.html")

def logout_user(request):
    logout(request)

    return redirect("products")
def fav(request):
    request.session["fav"] +=1
    return redirect("products")
# def delete(request,p_id):
#     item=models.item.objects.get(id=p_id)
#     item.delete()
#     return redirect("posts")
# def update(request,p_id):

    item=models.item.objects.get(id=p_id)
    item.delete()
    return redirect("posts") 

def counter(request):
    request.session['conter'] +=1
    return redirect("products")