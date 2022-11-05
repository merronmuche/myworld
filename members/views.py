from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.template import loader
from members.models import Members

def index(request):
  
  members = Members.objects.all()

  context = {
    'members':members
  }
  return render(request, 'members/myfirst.html', context)


def new_mod(request):
    Members.objects.create(firstname= 'markos',lastname='amsalu',age=30)
    return HttpResponse('Created successuulyly')


def add(request):
    
    if request.method == 'GET':
      return render(request, 'members/add.html')
    else:
        x = request.POST['first']
        y = request.POST['last']
        age = request.POST['age']
        Members.objects.create(firstname=x, lastname=y, age=age)
        return redirect(reverse('index'))


def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return redirect(reverse('index'))
  
