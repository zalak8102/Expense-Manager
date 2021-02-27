from django.shortcuts import render,redirect
from goal.models import goal,contribLog
from datetime import datetime
from datetime import time
import time
import math
# Create your views here.
def goals(request):
    currentDate = datetime.now().day
    gls=goal.objects.all().filter(user_id=request.session['usremail'])
    stat = {}
    for g in gls:
        if(g.amount==0):
            stat[g.goalId]=0
        else:
            stat[g.goalId] = (g.status / g.amount)*100
            stat[g.goalId] = math.ceil(stat[g.goalId])
    return render(request,'goal/goals.html',context={"gls":gls ,"stat":stat})

def contri(request):
     if(request.POST['id'] != "0"):
        id=request.POST['id']
        g=goal.objects.get(goalId=id)
        if((g.amount-g.status)<g.contribution):
            amount = g.amount - g.status
            g.status = g.amount
        else:
            g.status += g.contribution
            amount = g.contribution
        g.count += 1
        g.save()
        goal_id = id
        user_id=request.session['usremail']
        date=datetime.now()
        conlog=contribLog(user_id=user_id,amount=amount,date=date,goal_id=goal_id)
        conlog.save()
     return redirect('/goals/')

def addgoal(request):
    return render(request,'goal/addgoal.html')

def add_goal(request):
    glName=request.POST['glname']
    contr=request.POST['glcont']
    amount=request.POST['glamt']
    user_id=request.session['usremail']
    date=datetime.now()
    goaldetails=goal(user_id=user_id,goalName=glName,amount=amount,date=date,contribution=contr,status=0)
    goaldetails.save()
    return redirect('/goals/')

def del_goal(request):
    id=request.POST['id']
    goal.objects.get(goalId=id).delete()
    return redirect('/goals/')

def updateGoal(request):
    id=request.POST['id']
    g=goal.objects.get(goalId=id)
    return render(request,'goal/updgoal.html',context={"g": g})

def upd_goal(request):
    id=request.POST['id']
    g=goal.objects.get(goalId=id)
    g.goalName=request.POST['glname']
    g.contribution=request.POST['glcont']
    g.amount=request.POST['glamt']
    g.save()
    return redirect('/goals/')

