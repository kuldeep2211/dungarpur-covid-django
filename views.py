from django.shortcuts import render
from django.http import *
from covid19.models import *
from django.db.models import Sum

# Create your views here.
def index(request):
	l1 = covidinfo.objects.all().order_by('village')
	l2 = covidinfo.objects.aggregate(consum=Sum('confirmed'))
	l3 = covidinfo.objects.aggregate(acsum=Sum('active'))
	l4 = covidinfo.objects.aggregate(recsum=Sum('recovered'))
	l5 = covidinfo.objects.aggregate(deccsum=Sum('deceased'))
	data = {'data':l1, 'consum':l2, 'acsum':l3, 'recsum':l4, 'deccsum':l5}
	return render(request, 'index.html', data)

def banswara(request):
	l6 = bascoinfo.objects.get()
	bcon = {'bas':l6}
	return render(request, 'banswara.html', bcon)

def udaipur(request):
	l7 = udaicoinfo.objects.get()
	ucon = {'udai':l7}
	return render(request, 'udaipur.html', ucon)

def dprdetails(request):
    l8 = dcoinfo.objects.get()
    dcon = {'dpr':l8}
    return render(request, 'dprdetails.html', dcon)