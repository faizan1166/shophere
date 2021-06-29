from django.shortcuts import render,redirect
from .models import product, Contact, Buy
from math import ceil
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
from django.http import HttpResponse


def index(request):
    allProds = []
    catprods = product.objects.values('category')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def productView(request, id):
    Product = product.objects.filter(id=id)
    return render(request, "shop/productview.html", {'Product': Product[0]})


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        description = request.POST.get('description', '')
        if len(name)<2 or len(email)<2 or len(description)<4:
            messages.error(request, "Please Fill the Form Correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, description=description)
            contact.save()
            messages.success(request, "Your From Has Been Submitted ")
    return render(request, "shop/contact.html")


def buy(request, id):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        state = request.POST.get('state', '')
        pin = request.POST.get('pin', '')
        product_name = request.POST.get('product_name', '')
        price = request.POST.get('price', '')
        product_detail = request.POST.get('product_detail', '')
        product_detail1 = request.POST.get('product_detail1', '')
        if len(name) < 2 or len(email) < 2 or len(phone) < 10 or len(address) < 8 or len(state) < 4 or len(pin) < 3 :
            messages.error(request,"Please Fill Your Form Correctly")
        else:
            buy = Buy(name=name, email=email, phone=phone, address=address, state=state, pin=pin, product_name=product_name,price=price,product_detail=product_detail,product_detail1=product_detail1)
            buy.save()
            messages.success(request,"Your Order Has Been Submitted Successfully")
    Product = product.objects.filter(id=id)
    return render(request, "shop/buy.html", {'Product': Product[0]})


def searchMatch(query, item):
    if query in item.product_name.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    if len(allProds) == 0 or len(query) < 4:
        messages.error(request,"Please make sure to enter relevant search query")
    return render(request, 'shop/search.html',params)


def signup(request):
    if request.method=="POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if len(username) < 10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('/')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('/')

        if (password1 != password2):
            messages.error(request, " Passwords does not match")
            return redirect('/')

        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        messages.success(request, " Your Account has been successfully created")
        return redirect('/')
    else:
        return HttpResponse("Error")


def view_login(request):
    if request.method =="POST" :
        usern = request.POST['usern']
        password = request.POST['password']
        user = authenticate(username=usern, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            messages.error(request, "Invalid! Username Or Password")
            return redirect("/")
    else:
        return HttpResponse('not found')


def view_logout(request):
    logout(request)
    messages.success(request,"Logged Out")
    return redirect("/")




def orderview(request):
    orders=Buy.objects.values('email','product_name','price','product_detail','status')
    params={'orders': orders}
    return render(request, "shop/orders.html" , params)


