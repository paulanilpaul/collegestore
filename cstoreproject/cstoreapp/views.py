from django.http import HttpResponse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . models import foam
# Create your views here.
def index(request):
    #return HttpResponse("Hello world")
    return render(request,"index.html")

def detail(request):
    foamm=foam.objects.all()
    context={
        's':foamm
    }
    return render(request,'sdetail.html',context)
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('page')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')
    return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "password not matched")
            return redirect('register')
        #return redirect('/')
    return render(request, "register.html")
def addfoam(request):
    if request.method == 'POST':
        name = request.POST['name']
        date = request.POST['date']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        department = request.POST['department']
        courses = request.POST['courses']
        purpose = request.POST['purpose']
        materials = request.POST['materials']

        fo = foam(name=name, date=date, age=age, gender=gender, phone=phone, email=email,
                  address=address, department=department, courses=courses,
                  purpose=purpose,materials=materials)
        fo.save()
        return render(request, "foam.html")
    else:
        return render(request, "foam.html")

def pag(request):
    return render(request, "page.html")

def logout(request):
    auth.logout(request)
    return redirect('/')