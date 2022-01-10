from django.db.models.query_utils import Q
from re import I
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import book,member
from .forms import memberform
from django.db.models import Q

def registernew(request):
    a=memberform(request.POST)
    if a.is_valid():
        a.save()
    return render(request,'registernew.html',{'form':a})

def register(request):
    if request.method=='POST':
        obj=member()
        obj.us=request.POST['name']
        obj.email=request.POST['email']
        obj.password=request.POST['pass']
        obj.phn=request.POST['phn']
        obj.save()
    return render(request,'registerwithoutform.html')

def login(request):
    if request.method=="POST":
        try:
            m = member.objects.get(us=request.POST['us'])
            
            if m.password == request.POST['password']:
                return HttpResponseRedirect('/app1/master/')

            else:
                return HttpResponse("<h2><a href=''>You have entered wrong password </a></h2>")
        except:
            return HttpResponse("<h2><a href=''>no username found.</a></h2>")
    return render(request,'login.html')

def calc(request):
    if request.POST:
        val1 = request.POST['a1']
        val2 = request.POST['a2']
        opt1 = request.POST['a3']
        if opt1 == 'sum':
            var = float(val1) + float(val2)
            var1=int(var)
            #return render(request,'index.html',{'ans':var,'val1':val1,'val2':val2})
            return HttpResponseRedirect(f'/app1/new/{var1}')

        elif opt1 == 'minus':
            var = float(val1) - float(val2)
            return render(request,'index.html',{'ans':var,'val1':val1,'val2':val2})

        elif opt1 == 'multi':
            var = float(val1) * float(val2)
            return render(request,'index.html',{'ans':var,'val1':val1,'val2':val2})

        elif opt1 == 'division':
            var = float(val1) / float(val2)
            return render(request,'index.html',{'ans':var,'val1':val1,'val2':val2})
            
    return render(request,'index.html')

def newfun(request,id):
    return HttpResponse(f'hello:{id}')

def pro(request):
    if request.GET:
        no1 = request.GET['n1']
        opt = request.GET['n3']
        if opt == 'gro':
            var1 = float(no1)*10/100
            var2=float(no1)+float(var1)
            return render(request,'product.html',{'n4':var1,'no1':no1,'ans':var2})

        elif opt == 'ele':
            var1 = float(no1)*18/100
            var2=float(no1)+float(var1)
            return render(request,'product.html',{'n4':var1,'no1':no1,'ans':var2})

        elif opt == 'clo':
            var1 = float(no1)*6/100
            var2=float(no1)+float(var1)
            return render(request,'product.html',{'n4':var1,'no1':no1 ,'ans':var2})

        elif opt == 'sta':
            var1 = float(no1)*12/100
            var2=float(no1)+float(var1)
            return render(request,'product.html',{'n4':var1,'no1':no1,'ans':var2})
            
    return render(request,'product.html')

def odd(request):
    if request.GET:
        i=int(request.GET['a'])
        print(i)
        if i%2==0:
            return HttpResponse(f"{i} is even")
        else:
            return HttpResponse(f"{i} Is odd")

    return render(request,'odd.html')

def table(request):
    if request.GET:
        num1=dict()
        no=int(request.GET['t'])
        for i in range(1,11):
            num1[i]=(f'{no} * {i} = {no*i}')   
        return render(request,"table.html",{'result':num1})

    return render(request,"table.html")

def student(request):
    
    return render(request,'student.html')

def master(request):
    b=book.objects.all()
    q = request.GET.get('search')
    if q:
        book1= book.objects.filter(Q(bookname1__icontains=q) | Q(des1__icontains=q))
        c = {
            'b1' : book1,
            }
    else:
        c={'b':b}
    return render(request,'master.html',c)

def about(request):
    obj1=book.objects.all()
    s=request.GET.get('search')
    if s:
        q=book.objects.filter(Q(bookname1__icontains=s |  Q(des1__icontains=s)))
    else:
        q=book.objects.all()
    return render(request,'about.html',{'book':obj1,'s':q})

def contact(request):
    return render(request,'contact.html')

def r(request):
    if request.method=='POST':
        obj=member()
        obj.us=request.POST['name']
        obj.email=request.POST['email']
        obj.password=request.POST['pass']
        obj.phn=request.POST['phn']
        obj.save()
    return render(request,'r.html')

def bookviewpr(request,pk):
    obj1=get_object_or_404(book,pk=pk )
    return render(request,'bookviewpr.html',{'b2':obj1})

def services(request):
    return render(request,'services.html')


def a(request):
    return render(request,'a.html')

def b(request):
    return render(request,'b.html')

def bookview(request):
    b=book.objects.all()
    return render(request,'book.html',{'b':b})


def prime(request):
    if request.GET:
        no=int(request.GET['p'])
        i=2
        f=0
        while i<no:
            if no%i==0:
                f=1
                break
            i=i+1
        if f==0:
            return HttpResponse(f'{no} is prime')
        else:
            return HttpResponse(f"{no} is not prime")
    return render(request,'prime.html')

def fec(request):
    if request.GET:
        no=int(request.GET['p'])
        a=1
        i=1
        while i<no:
            a=a*i
            i+=1
        return render(request,'fec.html',{'ans':a,'no':no})

    return render(request,'fec.html')


def search(request):
    try:
        q = request.GET.get('search')
    except:
        q = book.objects.all()
    if q:
        book1= book.objects.filter(Q(bookname1__icontains=q) | Q(des1__icontains=q))
        data = {
            'b1' : book1
        }
    else:
        data={}
    return render(request, 'search.html',data)
