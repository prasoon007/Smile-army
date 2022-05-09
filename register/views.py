from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse, request
from home import views
from .models import new_profile

# Create your views here.
def register(request):
    if(request.method=="POST"):
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        uname=request.POST['uname']
        address=request.POST['address']
        password=request.POST['password']
        conpassword=request.POST['conpassword']
        Phone=request.POST['phone']
        regname=request.POST['regname']
        

        if(password==conpassword):
            if User.objects.filter(username=uname).exists():
                messages.info(request,"opps! Username already taken.")
                return redirect("about")

            else:
                user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=password)
                if "staff" in request.POST:
                    user.is_staff=True
                    user.save()
                    user2=new_profile(user=user, contact_no=Phone,address=address, regname=regname)
                    user2.save()
                    messages.info(request,"congrates you are in..")
                    return redirect("login")
    return render(request,"staffreg.html")

def userreg(request):
    if(request.method=="POST"):
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        uname=request.POST['uname']
        password=request.POST['password']
        conpassword=request.POST['conpassword']
        Phone=request.POST['phone']

        if(password==conpassword):
            if User.objects.filter(username=uname).exists():
                messages.info(request,"opps! Username already taken.")
                return redirect("about")

            else:
                user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=password)
                user.save()
                user2=new_profile(user=user, contact_no=Phone)
                user2.save()
                messages.info(request,"congrates you are in..")
                return redirect("login")
    return render(request,"registration.html")

def login(request):
    if(request.method=="POST"):
        uname=request.POST["uname"]
        password=request.POST["password"]
        logger=auth.authenticate(username=uname,password=password)
        if logger!=None:
            auth.login(request,logger)
            return redirect("index")
        else:
            return redirect("login")
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("login")

def profile(request):
    display={}
    prof=new_profile.objects.filter(user__id=request.user.id)
    if len(prof)>0:
        dis=new_profile.objects.get(user__id=request.user.id)
        display["data"]=dis
    return render(request, "updateprofile.html",display)

def updateprofile(request):
    display={}
    prof=new_profile.objects.filter(user__id=request.user.id)
    if len(prof)>0:
        dis=new_profile.objects.get(user__id=request.user.id)
        display["data"]=dis
        

        if request.method=="POST":
            fname=request.POST['fname']
            lname=request.POST['lname']
            uname=request.POST['uname']
            email=request.POST['email']
            phone=request.POST['phone']
            address=request.POST['address']
            aadhar_id=request.POST['aadhar_id']
            state=request.POST['state']
            pin=request.POST['pin']
            city=request.POST['city']
            password=request.POST['password']
            conpassword=request.POST['conpassword']

            user=User.objects.get(id=request.user.id)
            user.username=uname
            user.first_name=fname
            user.last_name=lname
            user.email=email
            user.save()

            dis.aadhar_id=aadhar_id
            dis.phone=phone
            dis.city=city
            dis.address=address
            dis.state=state
            dis.save()

            if 'img' in request.FILES:
                image=request.FILES['img']
                dis.profile_picture=image
                dis.save()
                messages.info(request,"Image upload successfully")
            messages.info(request,"profile updata successfully")
        return render(request,"profile.html",display)

