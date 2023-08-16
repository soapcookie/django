from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from datetime import datetime

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    now = datetime.now()
    context ={
        'current_date' : now
    }
    return HttpResponse(template.render(context, request))



def select(request):
    message = "호준찌 힘내!!"
    return HttpResponse(message)


def result(request):
    message = "내가 성공해서 퐁퐁해줄게"
    return HttpResponse(message)