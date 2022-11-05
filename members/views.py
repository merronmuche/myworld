from django.http import HttpResponse
from django.shortcuts import render
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
