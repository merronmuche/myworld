from django.http import HttpResponse
from django.template import loader
from members.models import Members

def index(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())
def new_mod(request):
    Members.objects.create(firstname= 'markos',lastname='amsalu',age=30)
    return HttpResponse('Created successuulyly')
