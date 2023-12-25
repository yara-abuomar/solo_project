from django.db import models
import re
from datetime import date

class UserManager(models.Manager):
    def basic_validater(self,postData):
        errors={}
        if len(postData['fname'])<2:
            errors['fname']="firstname should be 2 char atleast"
        fname_regex=re.compile(r'^[a-zA-Z]')
        if not fname_regex.match(postData['fname']):
            errors['fname']="firstname should be char only "
        if len(postData['lname'])<2:
            errors['lname']="lastname should be 2 char atleast"       
        lname_regex=re.compile(r'^[a-zA-Z]')
        if not lname_regex.match(postData['lname']):
            errors['lname']="lastname should be char only "
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):         
            errors['email'] = "Invalid email address!"
        if len(User.objects.filter(email=postData['email']))>0:
            errors['email']="Email should be unieq!"
        if len(postData['pass'])<8:
            errors['pass']="password should be 8 char atleast"
        if postData['pass'] != postData['confirm']:
            errors['confirm']="password dont match"
        if len(postData['birth'])<1:
            errors['birth']="Birthday should added"
        if len(postData['uni'])<1:
            errors['uni']="University name should be added"
        if len(postData['edu'])<1:
            errors['edu']="Education background should be added"
        return errors
        

        

class JobManager(models.Manager):
    def validation(self,postData):
        error={}
        if len(postData['jname'])<1:
            error['jname']="job name  should be added"
        if len(postData['cat'])<1:
            error['cat']="job type should be added"
        if len(postData['Salary1'])<1:
            error['Salary1']="salary should be added"
        
        #sala=int(postData['Salary1'])
        #print(sala)
        #if sala < 1:
          #  error['Salary1']="salary should be more than 0"
        if len(postData['details'])<8:
            error['details']="description  should be 8 char atleast"

        if len(postData['cname'])<1:
            error['cname']="company name  should be added"
        return error
    

class CompanyManager(models.Manager):
    def validaterr(self,postData):
        error11={}
        if len(Company.objects.filter(name=postData['cname']))>0:
            error11['cname']="Company name  should be unieq!"
        if len(postData['cname'])<1:
            error11['cname']="Company name should be added"
        if len(postData['add'])<1:
            error11['add']="address should be added"
        return error11
     
class User(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    email=models.CharField(max_length=45)
    password=models.CharField(max_length=45)
    birthday=models.DateField(("Date"), default=date.today)
    university_name=models.CharField(max_length=45)
    education_background=models.CharField(max_length=45)
    gender=models.CharField(max_length=45,default="male")
    is_admin=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()

    def admin():
        if User.id == 1:
            is_admin=0
            return is_admin
        else:
            is_admin=1 
            return is_admin

    def add_user(first,last,email1,pass1,uni1,edu1,birth1,gndr):    
        User.objects.create(first_name=first,last_name=last,email=email1,password=pass1,university_name=uni1,education_background=edu1,birthday=birth1,is_admin=User.admin(),gender=gndr)


class Category(models.Model):
    type=models.CharField(max_length=45)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def read_all_category():
        return  Category.objects.all()
    
class Company(models.Model):
    name=models.CharField(max_length=45 , default="company")
    addres=models.CharField(max_length=45 , default="company")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=CompanyManager()

    def read_all_company():
        return  Company.objects.all()
    def add_Company(comname,addres1):
        Company.objects.create(name=comname,addres=addres1)
    
class Job(models.Model):
    job_name=models.CharField(max_length=45)
    job_details=models.TextField()
    salary=models.IntegerField()
    picture=models.FilePathField(null=True)
    category=models.ForeignKey(Category ,related_name="jobs_category",on_delete=models.CASCADE)
    company=models.ForeignKey(Company ,related_name="jobs_company",on_delete=models.CASCADE)
    users_apply=models.ManyToManyField(User,related_name="applid_jobs")
    Liks=models.ManyToManyField(User,related_name="like_jobs")
    due_date=models.DateTimeField(auto_now_add=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=JobManager()

    def addjob(jobname,comname,salry,description,jobtype,duedate,image):
        print("hiiii")
        print(comname)
        Job.objects.create(job_name=jobname,job_details=description,company=Company.objects.get(id=int(comname)),salary=salry,category=Category.objects.get(id=int(jobtype)),due_date=duedate,picture=image)
    def alljob():
        return Job.objects.all().order_by("-created_at")
    def delete_jop(id):
        job1=Job.objects.get(id=int(id))
        return job1.delete()
    



   


