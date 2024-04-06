from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def home (request,PK):
    # return HttpResponse ('<h1> This is Home Page </h1>')
    value = PK
    return render(request, 'index.html',{'data':value})  
def combination(request,string,ab,slugdata):
    data={
        'data1' : ab,
        'data2' : string,
        'data3' : slugdata,
    }
    return render(request, 'index.html',{'key':data})

