import email
from pyexpat import model
from django.db import models
import datetime
from django.core.validators import MaxValueValidator


# Create your models here.



class Account(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=12)
    whatsapp_no = models.CharField(max_length=12)
    gender = models.CharField(max_length=25)
    Date_of_birth = models.DateField()
    state = models.CharField(max_length=40)
    district = models.CharField(max_length=40)
    college_state = models.CharField(max_length=50)
    college = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    branch = models.CharField(max_length=40)
    passing_year = models.CharField(max_length=5)
    enrolment = models.CharField(max_length=20,default="Not Generated")
    payment_status = models.CharField(max_length=20,default="Null")
    # def nowdate():
    #     t = datetime.date.today
    #     return t
    created_at = models.DateTimeField(auto_now_add=True)
    Apply_status = models.CharField(max_length=10,default=0)
    
    

    # def 24hrslater():
    #     return datetime.date.today() + datetime.timedelta(days=1)

    
    

    # def now1():
    #     m = datetime.datetime.now()
    #     return m.strftime('%Y-%m')
    # created_at_month = models.CharField(default=datetime.datetime.now().strftime('%Y-%m'),max_length=10)


    def _str_(self):
        return self.fullname
class Career(models.Model):  
    Name =  models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Apply_status = models.CharField(max_length=10)
class Passcode(models.Model):
    code =  models.CharField(max_length=100)
    code_type = models.CharField(max_length=100)
    valid_date = models.DateField()
class Opening(models.Model):
    job = models.CharField(max_length=100)
    job_type =  models.CharField(max_length=200,default="Null") 
    
class College(models.Model):
    college_name =  models.CharField(max_length=200)
    college_state =  models.CharField(max_length=200,default="Null")  
    Apply_status = models.CharField(max_length=10)


class Dashboarduser(models.Model):
    username =  models.CharField(max_length=200) 
    password = models.CharField(max_length=10)
    cnf_password = models.CharField(max_length=10)


class Voucher(models.Model):
    voucher_code =  models.CharField(max_length=200) 
    price = models.CharField(max_length=10)
    status = models.CharField(max_length=10)



  
    

