from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from happybackapp.models import adminregdb,gallerydb,pricingdb,bookingdb,contactdb


# Create your views here.
def indexpage(req):
    return render(req,"index.html")
def addadmin(req):
    return render(req,"addadmin.html")
def saveadminpage(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        mob = request.POST.get('mobile')
        user = request.POST.get('username')
        password = request.POST.get('password')
        img = request.FILES['image']
        obj = adminregdb(NAME=na, EMAIL=em, MOBILE=mob, USERNAME=user, PASSWORD=password, IMAGE=img)
        obj.save()
        return redirect(addadmin)
def displayadmin(req):
    data = adminregdb.objects.all()
    return render(req,"displayadmin.html",{'data':data})
def editadmin(req,dataid):
    data = adminregdb.objects.get(id=dataid)
    print(data)
    return render(req,"editadmin.html",{'data':data})
def updateadmin(req,dataid):
    if req.method == "POST":
        na = req.POST.get('name')
        email = req.POST.get('email')
        mob = req.POST.get('mobile')
        uname = req.POST.get('username')
        passwrd = req.POST.get('password')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = adminregdb.objects.get(id=dataid).IMAGE
        adminregdb.objects.filter(id=dataid).update(NAME=na, EMAIL=email, MOBILE=mob, USERNAME=uname, PASSWORD=passwrd, IMAGE=file)
        return redirect(displayadmin)
def deleteadmin(req,dataid):
    data = adminregdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayadmin)




def gallery(req):
    return render(req, "gallery.html")
def savegallery(request):
        if request.method == "POST":
            tl = request.POST.get('Title')
            na = request.POST.get('Name')
            img = request.FILES['image']
            obj = gallerydb(NAME=na, TITLE=tl, IMAGE=img)
            obj.save()
            return redirect(gallery)
def displaygallery(req):
    data = gallerydb.objects.all()
    return render(req,"displaygallery.html",{'data':data})
def editgallery(req,dataid):
    data = gallerydb.objects.get(id=dataid)
    print(data)
    return render(req,"editgallery.html",{'data':data})
def updategallery(req,dataid):
    if req.method == "POST":
        na = req.POST.get('Name')
        tl = req.POST.get('Title')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = gallerydb.objects.get(id=dataid).IMAGE
        gallerydb.objects.filter(id=dataid).update(NAME=na, TITLE=tl, IMAGE=file)
        return redirect(displaygallery)
def deletegallery(req,dataid):
    data = gallerydb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaygallery)
def pricing(req):
    return render(req,"pricing.html")
def savepricing(request):
    if request.method == "POST":
        na = request.POST.get('Name')
        ph = request.POST.get('Photos')
        ca = request.POST.get('Camera')
        te = request.POST.get('Term')
        pr = request.POST.get('Pricing')
        # img = request.FILES['image']
        obj = pricingdb(NAME=na, PHOTOS=ph, CAMERA=ca, TERM=te, PRICING=pr,)
        obj.save()
        return redirect(pricing)
def displaypricing(request):
    data = pricingdb.objects.all()
    return render(request,"displaypricing.html",{'data':data})
def editpricing(req,dataid):
    data = pricingdb.objects.get(id=dataid)
    print(data)
    return render(req,"editpricing.html",{'data':data})
def updatepricing(req,dataid):
    if req.method == "POST":
        na = req.POST.get('Name')
        ph = req.POST.get('Photos')
        ca = req.POST.get('Camera')
        te = req.POST.get('Term')
        pr = req.POST.get('Pricing')
        # try:
        #     img = req.FILES['image']
        #     fs = FileSystemStorage()
        #     file = fs.save(img.name,img)
        # except MultiValueDictKeyError:
        #     file = pricingdb.objects.get(id=dataid).IMAGE
        pricingdb.objects.filter(id=dataid).update(NAME=na, PHOTOS=ph, CAMERA=ca, TERM=te, PRICING=pr, )
        return redirect(displaypricing)
def deletepricing(req,dataid):
    data = pricingdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaypricing)




def loginpage(req):
    return render(req, "loginpage.html")
def adminloginpage(req):
    if req.method == "POST":
        username_r = req.POST.get('username')
        password_r = req.POST.get('pass')

        if User.objects.filter(username__contains = username_r).exists():
            user = authenticate(username = username_r, password=password_r)
            if user is not None:
                login(req,user)
                req.session['username']=username_r
                req.session['pass']=password_r
                return redirect(indexpage)
            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)


def viewbooking(request):
    data = bookingdb.objects.all()
    return render(request, "viewbooking.html", {'data': data})
def deletebooking(req,dataid):
    data = bookingdb.objects.filter(id=dataid)
    data.delete()
    return redirect(viewbooking)


def viewcontact(request):
    data = contactdb.objects.all()
    return render(request, "viewcontact.html", {'data': data})
def deletecontact(req,dataid):
    data = contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(viewcontact)