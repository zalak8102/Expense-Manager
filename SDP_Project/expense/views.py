from django.shortcuts import render,redirect
from expense.models import expense
from income.models import income_details
from goal.models import contribLog
from django.contrib import messages
import math
import operator
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
from datetime import datetime

# Create your views here.
def calculate(request):
    exps=expense.objects.all().filter(user_id=request.session['usremail'])
    total_exp=0
    total_inc=0
    total_conl=0
    count=0
    average=0
    rexp=0
    amt=[]
    for ep in exps:
        total_exp+=ep.amount
        amt.append(ep.amount)
        count=count+1
    average=total_exp/count
    incs=income_details.objects.all().filter(user_id=request.session['usremail'])
    for ic in incs:
        total_inc+=ic.amount
    conlog=contribLog.objects.all().filter(user_id=request.session['usremail'])
    for cl in conlog:
        total_conl+=cl.amount
    rexp=(total_exp/total_inc)*100
    rexp = math.ceil(rexp)
    total=total_inc-total_exp-total_conl
    rsave = ((total)/total_inc)*100
    rsave = math.ceil(rsave)
    if total_exp > total_inc :
        safe = False
    else:
        safe = True
    currentMonth = datetime.now().month
    eps={"currentMonth":currentMonth,"safe":safe,"exps":exps,"total_exp":total_exp,"texp":total_exp,"total_inc":total_inc,"average":average,"rexp":rexp,"rsave":rsave,"total":total}
    return eps

def sortByDate(request):
    exps=expense.objects.all().filter(user_id=request.session['usremail']).order_by('date')
    eps=calculate(request)
    return render(request,'expense/expense.html',context={"currentMonth":eps["currentMonth"],"exps": exps,"safe":eps["safe"]})

def sortByAmt(request):
    exps=expense.objects.all().filter(user_id=request.session['usremail']).order_by('amount')
    eps=calculate(request)
    return render(request,'expense/expense.html',context={"currentMonth":eps["currentMonth"],"exps": exps,"safe":eps["safe"]})

def sortByCate(request):
    exps=expense.objects.all().filter(user_id=request.session['usremail']).order_by('category')
    eps=calculate(request)
    return render(request,'expense/expense.html',context={"currentMonth":eps["currentMonth"],"exps": exps,"safe":eps["safe"]})

def exp(request):
    exps=expense.objects.all().filter(user_id=request.session['usremail'])
    eps=calculate(request)
    return render(request,'expense/expense.html',context={"exps": exps,"safe":eps["safe"],"currentMonth":eps["currentMonth"]})

def report(request):
    exps=expense.objects.all().filter(user_id=request.session['usremail'])
    labels = 'Food', 'Entertainment','HouseHold','Medical','Shopping','Travel','Others'
    #labels = 'F','E','H','M','S','T','O'
    catamt = {
        "food": 0,
        "entertainment": 0,
        "household": 0,
        "medical": 0,
        "shopping":0,
        "travel":0,
        "others":0
    }
    if request.method == "POST":
        date1 = request.POST['from']
        date2 = request.POST['to']
        exps2 = exps.filter(date__range=[date1, date2])
        for e in exps2:
            catamt[e.category] += e.amount
    else:
        for e in exps:
            catamt[e.category] += e.amount
    f = False
    for c in catamt:
        if catamt[c]:
            f = True
    if f:
        sizes = []
        for key in catamt:
            sizes.append(catamt[key])
        objects = labels
        y_pos = np.arange(len(objects))
        qty = sizes
        plt.bar(y_pos, qty, align='center', alpha=0.5)
        plt.xticks(y_pos,objects,rotation='vertical')
        plt.ylabel('Amount')
        plt.title('Category')
        plt.savefig('media/chart.png',bbox_inches = "tight")
        plt.clf()
        
    eps=calculate(request)
    l1=[]
    for c in catamt:
        if catamt[c]:
            l1.append(catamt[c])
    min_exp=min(l1)
    max_exp=max(l1)
    eps["min_exp"] = min_exp
    eps["max_exp"] = max_exp
    eps["cmtamt"] = catamt
    eps["total_exp"] = sum(l1)
    eps["f"]=f
    return render(request,'expense/report.html',eps)

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
    label=['food', 'entertainment','household','medical','shopping','travel','others']
    label.remove(exps.category)
    return render(request,'expense/updateExp.html',context={"exps": exps,"label":label})


def upd_exp(request):
    id=request.POST['id']
    exps=expense.objects.get(expId=id)
    exps.expName=request.POST['expnm']
    exps.comments=request.POST['expcmt']
    exps.amount=request.POST['expamnt']
    exps.user_id=request.session['usremail']
    exps.category=request.POST['catg']
    exps.date=request.POST['expdt']
    exps.save()
    return redirect('/exp/')

def del_exp(request):
    id=request.POST['id']
    expense.objects.get(expId=id).delete()
    return redirect('/exp/')



