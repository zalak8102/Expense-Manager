from django.shortcuts import render,redirect
from signup.models import user_details
from django.contrib import messages

# Create your views here.

def home(request):
    #l={}
    #l.update(csrf(request))
    return render(request,'home.html')

def register(request):
    return render(request,'signup/register.html')

def login(request):
    return render(request,'signup/login.html')

def user_register(request):
    email=request.POST['uemail']
    pswd=request.POST['pwrd']
    cpswd=request.POST['cpwrd']
    uname=request.POST['usrne']
    bdate=request.POST['bdate']
    gender=request.POST['gen']
    if pswd==cpswd:
        usrdetails=user_details(email=email,password=pswd,username=uname,bdate=bdate,gender=gender)
        usrdetails.save()
        return render(request,'signup/login.html')
    else:
        messages.warning(request,"Enter proper password!!")
        return render(request,'signup/register.html')

def signin(request):
    usremail=request.POST['ueml']
    pswd=request.POST['upswd']
    ch=user_details.objects.all()
    for user in ch:
        if user.email==usremail:
            if user.password==pswd:
                count=1
                break
            else:
                count=0
                break
        else:
            count=-1
    if count==1:
        request.session['usremail']=usremail
        return redirect('/income/income/')
    elif count==0:
        messages.warning(request,"Incorrect password!!")
        return render(request,'signup/login.html')
    elif count==-1:
        messages.warning(request,"account does'nt exists!!")
        return render(request,'signup/login.html')

def logout(request):
    if request.session['usremail']:
        del request.session['usremail']
        messages.warning(request,"Logged Out")
        return render(request,'home.html')
    else:
        return render(request,'home.html')
    
def profile(request):
    if 'usremail' in request.session:
        usr=user_details.objects.get(email=request.session['usremail'])
        return render(request,'signup/profile.html',context={"usr": usr})
    else:
        return render(request,'signup/login.html')

def updateprf(request):
    email=request.POST['email']
    usr=user_details.objects.get(email=email)
    g=1
    if usr.gender == "male" :
        g=0
    return render(request,'signup/upd_profile.html',context={"usr": usr,"g":g})

def upd_profile(request):
    email=request.session['usremail']
    usr=user_details.objects.get(email=email) 
    #pswd=request.POST['pwrd']
    #cpswd=request.POST['cpwrd']
    usr.username=request.POST['usrne']
    usr.bdate=request.POST['bdate']
    usr.gender=request.POST['gen']
    usr.save()
    return redirect('/signup/profile')