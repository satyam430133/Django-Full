# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import usersFormzzz    
from service.models import service
from news.models import News

def home(request):
    return render(request, 'index.html')
def servicedata(request):
    searchfill = ''
    s = service.objects.all()
    # s = service.objects.all().order_by('-id') this syntax for giving the order form to data 
    # s = service.objects.all().order_by('-id')[2:5]  this syntax for slicing of data 
    newzz = News.objects.all()
    if request.method == 'POST':
        st = request.POST.get('search')
        if st!= None:
           s = service.objects.filter(service_title__icontains=st)
        #    s = service.objects.filter(service_title=st) to filter the data  y title but you have to put whole title accurate
        elif request.POST.get('search') == '' or None:
            return render (request, 'servicedata.html',data)
            s = service.objects.all()
    data = {
        'serviceData':s,
        'newsinfo':newzz,
    }
    return render(request, 'service.html',data)
def newsdetails(request,newsid):
    newzdetail = News.objects.get(id = newsid)
    data = {
        'newzdetail':newzdetail
    }
    return render (request, 'newsdetails.html',data)

# def urlll(request):
#     return redirect ("https://satyamm.shop/")
# def Homepage(request):
#     data = {    
#         'title': 'home new',
#         'bdata': 'jerry',
#         'clist': ['php','java','python'],
#         'num1':[10,20,30,40,50,60,70,80,90],
#         'num2':[],
#         'student_details':[
#             {'name':'predeep','phone':9893992626},
#             {'name':'testing','phone':9893992627}
#         ]
#     }
#     # return HttpResponse("Hello This is home page") 
#     return render (request, 'home.html',data)

def about(request):
    if request.method == 'GET':
        output= request.GET.get('output')
    return render(request, 'about.html',{'output':output})
# def aboutUs(request):
#     return HttpResponse("Welcome to My Website")
# def course(request):
#     return HttpResponse('<h1> Hello This is\
#                 is Course Page </h1>')
# def courceDetails(request,courceId):
#     return HttpResponse(courceId)
def userForm(request):
    try:
        ans = 0
        fn = usersFormzzz()
        data = {'form':fn}
        # username = int(request.GET['username'])
        # password = int(request.GET['password'])
        if request.method == 'POST':
         username = int(request.POST.get('username'))
         password = int(request.POST.get('password'))
         ans = username + password
         data = {
             'username':username,
             'password':password,
             'output':ans,
             'form':fn
             
         }
        #  url = '/about/?output={}'.format(ans)
        #  return redirect (url)
    except:
        pass
    return render (request,'userform.html',data)
# def submitform(request):
#      try:
#         ans = 0
#         data = {}
#         # username = int(request.GET['username'])
#         # password = int(request.GET['password'])
#         if request.method == 'POST':
#          username = int(request.POST.get('username'))
#          password = int(request.POST.get('password'))
#          ans = username + password
#          data = {
#              'username':username,
#              'password':password,
#              'output':ans,
             
#          }
#         #  url = '/about/?output={}'.format(ans)
#         #  return redirect (url)
#          return HttpResponse(ans)
#      except:
#         pass

def calculator(request):
    c = ''
    try:
        if request.method == "POST":
            n1 =  eval(request.POST.get('val1'))
            n2 =  eval(request.POST.get('val2'))
            opr =  request.POST.get('opr')
            if opr == '+':
                c = n1 + n2 
            elif opr == '-':
                c = n1 - n2
            elif opr == '*':
                c = n1 * n2
            elif opr == '/':
                c = n1 / n2
    except:
        pass
    return render (request,'calculator.html',{'c':c})
def evenOdd(request):
    ans = ''
    try:
        if request.method == 'POST':
            if request.POST.get('value') == '':
                return render (request, 'evenOdd.html',{'error':True})
            n1 = eval(request.POST.get('value'))
            if n1 % 2 == 0:
                ans = 'Even Number'
            else:
                ans = 'Odd Number'
    except:
        pass
    return render (request, 'evenOdd.html',{'ans':ans})
def marksheet(request):
    g = ''
    data = {}
    try:
        if request.method == 'POST':
            s1 = eval(request.POST.get('subject1'))
            s2 = eval(request.POST.get('subject2'))
            s3 = eval(request.POST.get('subject3'))
            t = s1+s2+s3
            p = t*100/300
            if p > 59 :
                g = 'A'
            elif p > 45:
                g = 'B'
            elif p > 33:
                g = 'C'
            else:
                g = 'Fail'
            data = {
                'total':t,
                'percentage':p,
                'grade':g
            }
    except:
        pass
    return render (request, 'marksheet.html',data)