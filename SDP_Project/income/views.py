from django.shortcuts import render,redirect
from income.models import income_details
from django.contrib import messages


# Create your views here.

def income(request):
    inc=income_details.objects.all().filter(user_id=request.session['usremail'])
    #for p in income_details.objects.raw('SELECT * FROM income_income_details'):
        #inc.append(p)
    return render(request,'income/income.html',context={"inc": inc})


def addinc(request):
    return render(request,'income/add_income.html')


def add_income(request):
    name=request.POST['iname']
    description=request.POST['ides']
    amount=request.POST['iamt']
    user_id=request.session['usremail']
    date=request.POST['idate']
    if 'ireg' in request.POST:
        regular = 1
    else:
        regular = 0
    incomedetails=income_details(name=name,description=description,amount=amount,date=date,user_id=user_id,regular=regular)
    incomedetails.save()
    return redirect('/income/income/')
   
def del_income(request):
    id=request.POST['id']
    income_details.objects.get(incomeID=id).delete()
    return redirect('/income/income/')

def updateinc(request):
    id=request.POST['id']
    inc=income_details.objects.get(incomeID=id)
    return render(request,'income/upd_income.html',context={"inc": inc})

def upd_income(request):
    id=request.POST['id']
    inc=income_details.objects.get(incomeID=id)
    inc.name=request.POST['iname']
    inc.description=request.POST['ides']
    inc.amount=request.POST['iamt']
    inc.user_id=request.session['usremail']
    inc.date=request.POST['idate']
    if 'ireg' in request.POST:
        inc.regular = 1
    else:
        inc.regular = 0
    inc.save()
    return redirect('/income/income/')