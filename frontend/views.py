from django.shortcuts import render,redirect

from happybackapp.models import gallerydb,pricingdb,bookingdb,contactdb
from frontend.models import logindb
from django.contrib import messages

# Create your views here.
def indexpg(req):
    data = gallerydb.objects.all()
    return render(req,"indexfd.html",{'data':data})
def gallerypg(req):
    data = gallerydb.objects.all()
    return render(req,"galleryfd.html",{'data':data})
def aboutpg(req):
    return render(req,"aboutfd.html")
def pricingpg(req):
    data = pricingdb.objects.all()
    return render(req,"pricingfd.html",{'data':data})
def bookingpg(request):
    if request.method == "POST":
        na = request.POST.get('name')
        da = request.POST.get('date')
        nu = request.POST.get('number')
        em = request.POST.get('email')
        ty = request.POST.get('type')
        obj = bookingdb(NAME=na, DATE=da, MOBILE=nu, EMAIL=em, TYPE=ty,)
        obj.save()
        messages.success(request,"Booked")
    return render(request,"bookingfd.html")
def contactpg(request):
    if request.method == "POST":
        na = request.POST.get('name')
        sb = request.POST.get('subject')
        me = request.POST.get('message')
        em = request.POST.get('email')
        obj = contactdb(NAME=na,  SUBJECT=sb, MESSAGE=me, EMAIL=em, )
        obj.save()
    return render(request,"contactfd.html")
def loginpg(request):
    return render(request, "loginfd.html")

def saveloginpg(request):
    if request.method == "POST":
        na = request.POST.get('name')
        pc = request.POST.get('password')
        ps = request.POST.get('password1 ')
        em = request.POST.get('email')
        obj = logindb(NAME=na, PASSWORD=pc, CONFIRMPASSWORD=ps, EMAIL=em)
        obj.save()
        return render(request,"loginfd.html")

def custemerlogin(request):
    if request.method=='POST':
        Username_r=request.POST.get("name")
        Password_r=request.POST.get("password")
        if logindb.objects.filter(NAME=Username_r,PASSWORD=Password_r).exists():
            request.session['name']=Username_r
            request.session['password']=Password_r
            messages.success(request, "Login Successfully...!")
            return redirect(indexpg)
        else:
            messages.error(request,"Invalid User..!")
            return render(request,'loginfd.html')
def userlogout(request):
    del request.session['name']
    del request.session['password']
    messages.success(request, "Logout Successfully...!")
    return redirect(indexpg)
