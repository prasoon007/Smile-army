from django.contrib import messages
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404, resolve_url
from django.http import HttpResponse, request
from .models import category, Services ,cart , Contact
from register.models import new_profile 
from django.http import JsonResponse ,HttpResponse

# Create your views here.
def index(request):
    cat=category.objects.all().order_by("cat_name")
    return render(request,"index.html",{'categ':cat})
def index2(request):
    return render(request,"index2.html")
def about(request):
    return render(request,"about.html")
def menu(request):
    return render(request,"menu.html")
def gallery(request):
    return render(request,"gallery.html")
def blog(request):
    return render(request,"blog.html")
def blog_single(request):
    return render(request,"blog_single.html")
def booking(request):
    if request.method=="POST":
        name=['name']
        phone=['phone']
        address=['address']
        bk=Services(name=name,address=address)
        bk.save()
        ph=Contact(phone=phone)
        ph.save()
    return render(request,"booking.html")

def contact(request):
    us=Contact.objects.filter(user_id=request.user.id)
    if request.method=="POST":
        phone=request.POST['phone']
        content=request.POST['message']
        print (phone, content)

        if  len(phone)<10 or len(content)<4:
            messages.info(request, "Field Error")
        else:
            usr=get_object_or_404(User,id=request.user.id)
            contact=Contact(user=usr, phone=phone, content=content)
            contact.save()
            return redirect("index")
            messages.info(request, "Message send successfullt...")     
    return render(request,"contact.html")

def confirmation(request):
    return render(request,"confirmation.html")
def term(request):
    return render(request,"terms.html")
def policy(request):
    return render(request,"policy.html")
def login(request):
    return render(request,"login.html")
def register(request):
    return render(request,"registration.html")
def profile(request):
    return render(request,"profile.html")
def updateprofile(request):
    return render(request,"updateprofile.html")

def Service(request, cid):
    cat=category.objects.get(id=cid)
    food=Services.objects.filter(cate=cat).order_by("id")
    return render(request,"services.html",{"food":food})        

def serve(request):
    se=Services.objects.filter().order_by("cate")
    ca=category.objects.all()
    return render(request,"serve.html",{"food":se,"dat":ca})

def search(request):
    if request.method=="GET":
        s=request.GET["copy"]
        sev=Services.objects.filter(name__icontains=s).order_by("name")
    return render(request,"search.html",{"sev":sev})


def addser(request):
    ads={}
    serv=category.objects.all()
    ads["serv"]=serv
    feeder=get_object_or_404(User,id=request.user.id)
    if request.method=="POST":
        name=request.POST["ser_name"]
        c=request.POST["cate"]
        address=request.POST["address"]
        quantity=request.POST["quant"]
        details=request.POST["details"]
        Category=category.objects.get(id=c)
        ap=Services(name=name,feeder=feeder,desc=details,Available_qunatitiy=quantity,cate=Category,address=address)
        ap.save()

        if "ser_img" in request.FILES:
            imgs=request.FILES("ser_img")
            ap.image=imgs
            ap.save()        
    return render(request,"addser.html",{"serv":serv})

def dashboard(request):
    aser=new_profile.objects.filter(user__id=request.user.id)
    if len(aser)>0:
        data=new_profile.objects.get(user__id=request.user.id)
    return render(request,"dashboard.html")       

def addtocart(request):
    dic={}
    it=cart.objects.filter(user__id=request.user.id, status="False")
    dic["item"]=it
    if request.user.is_authenticated:
        if request.method=="POST":
            sid=request.POST["atc"]
            quant=request.POST["qty"]
            is_exist=cart.objects.filter(imaging_id=sid, user_id=request.user.id, status="False")
            
            if len(is_exist)>0:
                dic["msg"]="item already exist in your cart."
            else:
                srvc=get_object_or_404(Services, id=sid)
                user=get_object_or_404(User, id=request.user.id)
                
                crt=cart(user=user,imaging=srvc,quantity=quant )
                crt.save()
                dic["msg"]="{} Add in your cart".format(srvc.name)
                dic["cls"]="alert sucess"
        else:
            dic["satuts"]="Please Login First to checkout"
    return render(request,"cart.html",dic)


def remove_product(request):
    if "quantity" in request.GET:
        cid = request.GET["cid"]
        qty = request.GET["quantity"]
        cart_obj = get_object_or_404(cart,id=cid)
        cart_obj.quantity = qty
        cart_obj.save()
    
        return HttpResponse(cart_obj.quantity)

    if "delete_cart" in request.GET:
        id=request.GET["delete_cart"]
        cartobject=get_object_or_404(cart,id=id)
        cartobject.delete()


        return HttpResponse(0)