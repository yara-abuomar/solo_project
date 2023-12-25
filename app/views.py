from django.shortcuts import render ,redirect
from.models import *
from django.contrib import messages
import bcrypt

def regestraion_form(request):
    return render(request,'login.html')

def newaccount(request):
    return render(request,'newaccount.html')

def display_homepage(request):
    if 'id' not in request.session:
        messages.error(request,"you must log in ")
        return redirect ('/')
    if request.session['id']==1:
        context={
            'which':1,
        }
        return render(request,'index.html',context)
    else:
        return render(request,'index.html')

    

def login(request):
    user1=User.objects.filter(email=request.POST['email'])
    if user1:
        user=user1[0]
        if bcrypt.checkpw(request.POST['pass'].encode(), user.password.encode()):
            request.session['id']=user.id
            request.session['name']=user.first_name
            return redirect('/home')
        else:
            messages.error(request,"incorrect username or password")
            return redirect ("/")
    else:
            messages.error(request,"incorrect username or password")
            return redirect ("/")

def regestration_user(request):
    errors=User.objects.basic_validater(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/newaccount')
    else:
        password=request.POST['pass']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.add_user(first=request.POST['fname'],last=request.POST['lname'],birth1=request.POST['birth'],uni1=request.POST['uni'],edu1=request.POST['edu'],email1=request.POST['email'],pass1=pw_hash ,gndr=request.POST['gendr'])
        return redirect('/')
def logout(request):
    request.session.flush()
    return redirect('/')

def aboutus(request):
    if 'id' not in request.session:
        messages.error(request,"you must log in ")
        return redirect ('/')
    if request.session['id']==1:
        context={
            'which':1,
        }
        return render(request,'about.html',context)
    else:
        return render(request,'about.html')
     

def postjob(request):
    if 'id' not in request.session:
        messages.error(request,"you must log in ")
        return redirect ('/')
    if request.session['id'] == 1:
        if request.session['id']==1:
            context={
            'which':1,
            'all_category': Category.read_all_category(),
            'all_com':Company.read_all_company(),
           }
            return render(request,'postjob.html',context)
        else:
            return render(request,'postjob.html')
    else: 
        messages.error(request,"you are not admin  ")
        return redirect('/')

   

def addjobs(request):
    error=Job.objects.validation(request.POST)
    if len(error)>0:
        for key,value in error.items():
            messages.error(request,value)
        return redirect('/postjob')
    else:
        Job.addjob(jobname=request.POST['jname'],comname=request.POST['cname'],salry=request.POST['Salary1'],description=request.POST['details'],jobtype=request.POST['cat'],duedate=request.POST['due'],image=request.POST['pic'])
        return redirect('/jobs')
     
def jobspage(request):
    if 'id' not in request.session:
        messages.error(request,"you must log in ")
        return redirect ('/')
    if request.session['id']==1:
        context={
            'which':1,
            'alljob':Job.alljob(),
        }
        return render(request,'job-list.html',context)
    else:
        context={
            
            'alljob':Job.alljob(),
        }
        return render(request,'job-list.html',context)
    
def deletejob(request,id):
    Job.delete_jop(id)
    return redirect ('/jobs')

def edit(request,num):
    context={
        'onejob':Job.objects.get(id=int(num)),
        'all_category': Category.read_all_category(),
        'all_com':Company.read_all_company()

    }
    return render(request,'edit.html',context)

def edit_job(request,num1):
    error=Job.objects.validation(request.POST)
    if len(error)>0:
        for key,value in error.items():
            messages.error(request,value)
        return redirect('/edit/'+str(num1))
    else:
        job1=Job.objects.get(id=int(num1))
        job1.job_name=request.POST['jname']
        com1=request.POST['cname']
        job1.company=Company.objects.get(id=int(com1))
        job1.salary=request.POST['Salary1']
        job1.job_details=request.POST['details']
        cat1=request.POST['cat']
        job1.category=Category.objects.get(id=int(cat1))
        job1.save()
        return redirect ('/jobs')

def showmore(request,id1):
    if 'id' not in request.session:
        messages.error(request,"you must log in ")
        return redirect ('/')            
    if request.session['id']==1:
        context={
            'which':1,
            'this_job':Job.objects.get(id=int(id1)),
            
        }
        return render(request,'showmore.html',context)
    else:
        context={
        'this_job':Job.objects.get(id=int(id1)),
        }
        return render(request,'showmore.html',context)
    
def apply_job(request,id2):
    user1=User.objects.get(id=request.session['id'])
    job1=Job.objects.get(id=int(id2))
    job1.users_apply.add(user1)
    return redirect('/myjobs')

def myjobs_page(request):
    if 'id' not in request.session:
        messages.error(request,"you must log in ")
        return redirect ('/')
    if request.session['id']==1:
        context={
            'which':1,
            'one_user':User.objects.get(id=request.session['id']),
            
        }
        return render(request,'myjobs.html',context)
    else:
        context={
        'one_user':User.objects.get(id=request.session['id']),
        }
        return render(request,'myjobs.html',context)
    

    
def log(request):
    return render(request,'login.html')

def addcompany(request):
    error11=Company.objects.validaterr(request.POST)
    if len(error11)>0:
        for key,value in error11.items():
            messages.error(request,value)
        return redirect('/postjob')
    else:
        Company.add_Company(comname=request.POST['cname'],addres1=request.POST['add'])
        return redirect('/postjob')
    



    
def likeajob(request,id3):
    user1=User.objects.get(id=request.session['id'])
    job1=Job.objects.get(id=int(id3))
    job1.Liks.add(user1)
    return redirect('/myjobs')



def alljob(request):
    if 'id' not in request.session:
        messages.error(request,"you must log in ")
        return redirect ('/')
    if request.session['id'] == 1:
        if request.session['id']==1:
            context={
            'which':1,
            'alljobs': Job.objects.all()
           }
            return render(request,'alljob.html',context)
        else:
            return render(request,'alljob.html')
    else: 
        messages.error(request,"you are not admin  ")
        return redirect('/')
    
def addcat(request):
    Category.objects.create(type=request.POST['cat'])
    return redirect('/postjob')







  

