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
        #messages.warning(request,"Your are successfully logged in!!")
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
    
