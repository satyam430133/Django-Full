from django.shortcuts import render
from django.shortcuts import HttpResponse,render
from .models import *

# Create your views here.
def home(request):
    # newss = NewsModel.objects.all()
    # entry = StudentDetails.objects.create(Name='Satyam',City='Bhopal',Email='satyambadal48@gmail.com',Contact=6264263949)
    # entry1 = StudentDetails.objects.create(Name='sumit',City='indore',Email='sumit@gmail.com',Contact=6264263900)
    # entry2 = StudentDetails.objects.create(Name='rakesh',City='harda',Email='rakesh@gmail.com',Contact=6264263901)
    # entry3 = StudentDetails.objects.create(Name='abhishek',City='gwalior',Email='abhishek@gmail.com',Contact=6264263902)
    # entry4 = StudentDetails.objects.create(Name='anish',City='rewa',Email='anish@gmail.com',Contact=6264263903)
    filterrr = StudentDetails.objects.filter(Name__icontains='sumit')
    filterrr.update(Name="abhi")
    # print(filterrr)
    # filterrr = StudentDetails.objects.update(Name='rajesh')
    data={
    #     # 'newss':newss,
    #     # 'entry':entry,
        'filterrr':filterrr,
    }
    return render(request,'index.html',data)
