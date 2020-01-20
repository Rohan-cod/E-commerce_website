from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import Product,Contact
from math import ceil
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def index(request):
    prod=Product.objects.all()
    # print(prod)
    c=Product.objects.values("category")
    cats={i['category'] for i in c}
    cats=list(cats)
    cats.sort()
    # print(cats)
    lst=[]
    for cat in cats:
        product=Product.objects.filter(category=cat)
        # print(product)
        n=len(product)
        r=n//4 + ceil((n/4)-(n//4))
        nslides=range(1,r)
        lst.append([product,nslides])
        
    dctnry={'alldata':lst}
    return render(request,'shop/index.html',dctnry)

def contact(request):
    if request.method == "POST":
        name=(request.POST.get('name',''))
        email=(request.POST.get('email',''))
        phone=(request.POST.get('phone',''))
        selection=(request.POST.get('selection',''))
        desc=(request.POST.get('desc',''))
        contact=Contact(name=name,email=email,phone=phone,selection=selection,desc=desc)
        if(name != '' or email != '' or phone != '' or selection != '' or desc != ''):
            contact.save()
            return HttpResponseRedirect(reverse('index')) 
        return HttpResponseRedirect(reverse('contact'))   
        # print(name,email,phone,selection,desc)
    else:
        return render(request,'shop/contact.html')

def checkout(request):
    return render(request,'shop/cart.html')

def about(request):
    return render(request,'shop/about.html')

def register(request):
    if request.method == "POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        if(password1 == password2): 
            if User.objects.filter(username=username).exists():
               messages.info(request,'Username Taken! Try again.') 
               return HttpResponseRedirect(reverse('Register'))  
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Already registered! Try another.')
                return HttpResponseRedirect(reverse('Register'))
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save()
                return HttpResponseRedirect(reverse('index'))
        else:
            messages.info(request,'Password Mismatch! Re-confirm.')
            return HttpResponseRedirect(reverse('Register'))
    else:
        return render(request,'shop/register.html')

def productView(request,myid):
    product=Product.objects.filter(id=myid)
    # print(product)
    return render(request,'shop/product.html',{'product':product[0]})

def login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect(reverse('index'))
        else:
            print('invalid credintials')
            return HttpResponseRedirect(reverse('login'))
    else:
        return render(request,'shop/login.html')
    
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
