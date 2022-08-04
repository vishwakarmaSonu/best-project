from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from . models import contact
from . models import product
from . models import Booking
from . models import name
# Create your views here.
from .models import OrderForm


def open(request):
    custom = Booking.objects.all()
    cus_count = custom.count()
    cont = contact.objects.all()
    contact_count = cont.count()
    subscribe = name.objects.all()


    subscribe_count = subscribe.count()
    context = {'cus_count':cus_count,'contact_count':contact_count,'subscribe_count':subscribe_count}
    if request.method == "POST":
        if request.POST.get("name"):
            post = name()
            post.name = request.POST.get('name')
            post.save()
            return render(request, 'open.html',context)

    else:
      return render(request, 'open.html',context)


def login(request):
    if request.method=="POST":
        username1 = request.POST['username']
        password1 = request.POST['password']
        from django.contrib import auth
        user=auth.authenticate(username=username1,password=password1)
        if user is not None:
            auth.login(request, user)
            messages.success(request, " Thank you for login ")
            return render(request, 'open.html')
        else:
            messages.error(request, " You have entered wrong username and password ")
            return render(request, 'open.html')







    else:

       return render(request, 'login.html')

def singup(request):

    if request.method == 'POST':
        usernames = request.POST['username']
        firstnames = request.POST['first_name']
        lastnames = request.POST['last_name']
        emails = request.POST['email_ID']
        password = request.POST['password']
        if len(password)<5:
            messages.error(request, ' enter password greater than 5 digit ')
            return render(request, 'open.html')
        else:
           x = User.objects.create_user(username=usernames, first_name=firstnames, last_name=lastnames, email=emails,
                                         password=password)
           x.save()

           messages.success(request, ' successfully register')
           return redirect('/')

    else:
      return render(request, 'singup.html')

def touch(request):
    if request.method == "POST":
        if request.POST.get("name") and request.POST.get('phone') and request.POST.get('email') and request.POST.get(
                'message'):
            post = contact()
            post.name = request.POST.get('name')
            post.phone = request.POST.get('phone')
            post.email = request.POST.get('email')
            post.message = request.POST.get('message')
            if len(post.phone) < 9:
                messages.error(request, ' Invalid phone no.')
                return render(request, 'open.html')
            else:

                post.save()
                messages.success(request, " thank for contact me ")
                return render(request, 'open.html')
    else:



       return render(request,'contact.html',{})



def book(request):
    pros = product.objects.all()
    if request.method == "POST":
        if request.POST.get("name") and request.POST.get('phone') and request.POST.get('email') and request.POST.get(
                'address') and request.POST.get("item_id") and request.POST.get('item_name'):
            post = Booking()
            post.name = request.POST.get('name')
            post.phone = request.POST.get('phone')
            post.email = request.POST.get('email')
            post.address = request.POST.get('address')
            post.item_id = request.POST.get('item_id')
            post.item_name = request.POST.get('item_name')
            if len(post.phone) < 9:
                messages.error(request, ' Invalid phone no.')
                return render(request, 'open.html')
            else:

                post.save()
                messages.success(request, " successful booking")
                return render(request, 'open.html')
    else:



      return render(request, 'book.html',{'pros':pros})

def about(request):
    return render(request, 'about.html')

def owner(request):
    return render(request, 'owner.html')
def detail(request):

    customer = Booking.objects.all()
    form = OrderForm()
    if request.method == 'POST':
        # ('printing post:',requset.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form,'customer':customer}

    return render(request, 'detail.html',context)


def produc(request):
    products = product.objects.all()
    return render(request, 'product.html',{'products':products})
def logout(request):
    from django.contrib import auth
    auth.logout(request)
    messages.success(request,"LOGOUT")

    return redirect('/')
def booking(requrst,pk_test):
    customer = Booking.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()
    # context = {'customer':customer}
    context = {'customer': customer, 'orders': orders,'order_count':order_count}



    return render(requrst,'cus.html',context)