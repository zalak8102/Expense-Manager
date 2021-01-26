from django.shortcuts import render,redirect
from expense.models import expense
from django.contrib import messages

# Create your views here.
def exp(request):
    exps=expense.objects.all().filter(user_id=request.session['usremail'])
    return render(request,'expense/expense.html',context={"exps": exps})

def report(request):
    return render(request,'expense/report.html')

def addexp(request):
    return render(request,'expense/add_expense.html')

def add_expense(request):
    expName=request.POST['exname']
    comments=request.POST['excomt']
    amount=request.POST['examt']
    user_id=request.session['usremail']
    date=request.POST['exdate']
    category=request.POST['catg']
    expdetails=expense(expName=expName,category=category,amount=amount,date=date,comments=comments,user_id=user_id)
    expdetails.save()
    return redirect('/exp/')

def viewExp(request):
    id=request.POST['id']
    exps=expense.objects.get(expId=id)
    return render(request,'expense/view_exp.html',context={"exps": exps})

def updateExp(request):
    id=request.POST['id']
    exps=expense.objects.get(expId=id)
    return render(request,'expense/updateExp.html',context={"exps": exps})


def upd_exp(request):
    id=request.POST['id']
    exps=expense.objects.get(expId=id)
    exps.name=request.POST['expnm']
    exps.description=request.POST['expcmt']
    exps.amount=request.POST['expamnt']
    exps.user_id=request.session['usremail']
    exps.date=request.POST['expdt']
    exps.save()
    return redirect('/exp/')

def del_exp(request):
    id=request.POST['id']
    expense.objects.get(expId=id).delete()
    return redirect('/exp/')

