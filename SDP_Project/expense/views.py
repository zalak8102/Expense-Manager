from django.shortcuts import render,redirect
from expense.models import expense
from django.contrib import messages

# Create your views here.
def expense(request):
    return render(request,'expense/expense.html')

def report(request):
    return render(request,'expense/report.html')
