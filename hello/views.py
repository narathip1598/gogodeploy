from django.http import HttpResponse
from django.shortcuts import render
from .form import name
from .models import CreateBetLotto
from django.http.response import HttpResponse, HttpResponseRedirect

def loginForm(request):
    data=CreateBetLotto.objects.all()
    return render(request,'index.html',{'CreateBetLotto':data})

def betLotto(request):
    if request.method == 'POST':
        form = name(request.POST)
        if form.is_valid():
            numberLotto=request.POST['numberLotto']
            top = request.POST.get('top')
            down = request.POST.get('down')
            if top == 'on' and down == 'on':
                top = 1
                down = 1
            elif top == 'on' and down == None:
                top = 1
                down = 0
            elif top == None and down == 'on':
                top = 0
                down = 1
            else:
                top = 0
                down = 0
            price=request.POST['price']
            CreateBetLotto.objects.create(
                numberLotto=numberLotto,
                top=top,
                down=down,
                price=price
            )
            return HttpResponseRedirect('/')
    else: 
        form = name()
    return render(request,'bet.html',{'form':form})