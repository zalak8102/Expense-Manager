from django.shortcuts import render,redirect
from goal.models import goal

# Create your views here.
def goals(request):
    gls=goal.objects.all().filter(user_id=request.session['usremail'])
    return render(request,'goal/goals.html',context={"gls":gls})

def addgoal(request):
    return render(request,'goal/addgoal.html')

def add_goal(request):
    glName=request.POST['glname']
    contr=request.POST['glcont']
    amount=request.POST['glamt']
    user_id=request.session['usremail']
    date=request.POST['gldate']
    goaldetails=goal(user_id=user_id,goalName=glName,amount=amount,date=date,contribution=contr,status=0)
    goaldetails.save()
    return redirect('/goals/')
