from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.template import loader
from members.models import Members
from members.forms import MembersForm
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
      form = MembersForm()
      context = {
        'form':form
      }
      return render(request, 'members/add.html', context)
    else:
          
        form = MembersForm(request.POST)
        if form.is_valid():
          x =form.cleaned_data['firstname']
          y = form.cleaned_data['lastname']
          age = form.cleaned_data['age']
          Members.objects.create(firstname=x, lastname=y, age=age)
          return redirect(reverse('index'))


def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return redirect(reverse('index'))

def update(request, id):
    mymember = Members.objects.get(id=id)
    template = loader.get_template('members/update.html')
    context = {
      'mymember': mymember,
    }
    return HttpResponse(template.render(context, request)) 
