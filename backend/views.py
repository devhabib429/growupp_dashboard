from django.shortcuts import render,HttpResponse, HttpResponseRedirect,redirect
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .models import Account
from .models import Career
from .models import Opening
from .models import Passcode
from .models import College
from .models import Dashboarduser
from .models import Voucher
from django.template import loader
from .serializers import AccountSerializer
from .serializers import CareerSerializer
from .serializers import PasscodeSerializer
from .serializers import AccountopeningSerializer
from .serializers import CollegeSerializer
from .serializers import DashboardSerializer
from .serializers import VoucherSerializer
import datetime
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

# Create your views here.
class AccountViewset(ModelViewSet):
    serializer_class= AccountSerializer
    queryset = Account.objects.all()

class CareerViewset(ModelViewSet):
    serializer_class= CareerSerializer
    queryset = Career.objects.all()

class PasscodeViewset(ModelViewSet):
    serializer_class= PasscodeSerializer
    queryset = Passcode.objects.all()

class AccountopeningViewset(ModelViewSet):
    serializer_class= AccountopeningSerializer
    queryset = Opening.objects.all()
class CollegeViewset(ModelViewSet):
    serializer_class= CollegeSerializer
    queryset = College.objects.all()
class DashboardViewset(ModelViewSet):
    serializer_class= DashboardSerializer
    queryset = Dashboarduser.objects.all()
class VoucherViewset(ModelViewSet):
    serializer_class= VoucherSerializer
    queryset = Voucher.objects.all()


def login(request):
    temp = loader.get_template('dashboardlogin.html')  
    return HttpResponse(temp.render())


def index(request):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Account.objects.all().values()
        applied = Account.objects.filter(Apply_status="Applied")
        accept = Account.objects.filter(Apply_status="Accepted")
        reject = Account.objects.filter(Apply_status="Rejected")
        select = Account.objects.filter(Apply_status="Selected")
        pending = Account.objects.filter(Apply_status="Pending")
        amount_paid = Account.objects.filter(payment_status="success")
        amount_to_paid = Account.objects.filter(payment_status="Null")
        # applied = []
        # for account_applied in account:
        #     if account_applied.Apply_status ==  "Applied":
        #         applied.append(account_applied)
        # no_applied = len(append)
        
        totalaccount = len(list(account))
        no_applied = len(list(applied))
        no_accept = len(list(accept))
        no_reject = len(list(reject))
        no_select = len(list(select))
        no_pending = len(list(pending))

        no_of_paid = len(list(amount_paid))
        paid = 3000*no_of_paid


        to_be_paid = len(list(accept))
        tobepaid = 3000*to_be_paid

        context = {
            "total" : totalaccount,
            "applied": no_applied,
            "accept": no_accept,
            "reject": no_reject,
            "select": no_select,
            "pending": no_pending,
            "paid":paid,
            "tobepaid":tobepaid,
            "current_user":current_user
       }
        temp = loader.get_template('index.html')
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')
    return  render(request,"dashboardlogin.html")


#################### Passcode Page ##########################

def passcode(request):
    if 'user' in request.session:

        current_user = request.session['user']
        passcode = Passcode.objects.all().values()
        temp = loader.get_template('passcode.html')
        context = {
            "passcode" : passcode,
            "current_user": current_user
        }
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')

def addpasscode(request):

    x = request.POST['code']
    y = request.POST['codetype']
    z= request.POST['valid']
    passcode = Passcode(code=x, code_type=y,valid_date=z)
    passcode.save()
    return HttpResponseRedirect(reverse('passcode'))

def deletepasscode(request,id):
    delt = Passcode.objects.get(id=id)
    delt.delete()
    return HttpResponseRedirect(reverse('passcode'))

################# END PASSCODE ############################ 
################## Colleges Related #########################################
def colleges(request):
    if 'user' in request.session:
        current_user = request.session['user']
        college = College.objects.all().values()
        temp = loader.get_template('colleges.html')
        context = {
            "college" : college,
            "current_user" : current_user
        }
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')
def addcollege(request):

    x = request.POST['collegename']
    y = request.POST['status']
    college = College(college_name=x, Apply_status=y)
    college.save()
    return HttpResponseRedirect(reverse('colleges'))

def deletecollege(request,id):
    delt = College.objects.get(id=id)
    delt.delete()
    return HttpResponseRedirect(reverse('colleges'))

def updatecollege(request,id):
    updatepage = College.objects.get(id=id)
    temp = loader.get_template('updatecollege.html')
    context = {
        "updte" : updatepage
    }
    return HttpResponse(temp.render(context,request))


def updatecollegerecord(request,id):
    # if request.method == "post":
    first = request.POST.get("collegename")
    last = request.POST.get("status")
    col = College.objects.get(id=id)
    col.college_name = first
    col.Apply_status = last
    col.save()
    return HttpResponseRedirect(reverse('colleges'))
################## Colleges Related END #########################################
##################### Job Related ################################

def jobs(request):
    if 'user' in request.session:
        
        current_user = request.session['user']
        job = Opening.objects.all().values()
        temp = loader.get_template('jobs.html')
        context = {
            "jobs" : job,
            "current_user": current_user
        }
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')

def addjob(request):
    x = request.POST['job']
    y = request.POST['job_type']
    job = Opening(job=x,job_type=y)
    job.save()
    return HttpResponseRedirect(reverse('jobs'))


def deletejob(request,id):
    delt = Opening.objects.get(id=id)
    delt.delete()
    return HttpResponseRedirect(reverse('jobs'))
####################### End Job ##########################################
######################  VOUCHER ##############################33

def voucher(request):
    if 'user' in request.session:
        current_user = request.session['user']
        voucher = Voucher.objects.all().values()
        temp = loader.get_template('voucherlist.html')
        context = {
            "voucher" : voucher,
            "current_user" : current_user
        }
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')

def addvoucher(request):

    x = request.POST['vouchercode']
    y = request.POST['price']
    z = request.POST['status']
    voucher = Voucher(voucher_code=x, price=y,status=z)
    voucher.save()
    return HttpResponseRedirect(reverse('voucher'))

def deletevoucher(request,id):
    delt = Voucher.objects.get(id=id)
    delt.delete()
    return HttpResponseRedirect(reverse('voucher'))

def updatevoucher(request,id):
    updatepage = Voucher.objects.get(id=id)
    temp = loader.get_template('updatevoucher.html')
    context = {
        "updte" : updatepage
    }
    return HttpResponse(temp.render(context,request))

def updatevoucherrecord(request,id):
    # if request.method == "post":
    first = request.POST.get("vouchercode")
    last = request.POST.get("price")
    last1 = request.POST.get("status")
    v = Voucher.objects.get(id=id)
    v.voucher_code = first
    v.price = last
    v.status = last1
    v.save()
    return HttpResponseRedirect(reverse('voucher'))



######################END VOUCHER##########################33







##############################  Account Related  ######################################
def totalaccount(request):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Account.objects.all().values() 
        temp = loader.get_template('totalaccount.html')
        context = {
            "current_user":current_user,
            "accounts": account
        }
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')
def accountview(request,id):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Account.objects.get(id=id)
        temp = loader.get_template('accountview.html')
        context = {
            "acc_ind":account,
            "create_user" : current_user
        }
        
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')

def accountaccept(request,id):
    # if request.method == "post":
    accept = "Accepted"
    account = Account.objects.get(id=id)
    account.Apply_status = accept
    account.save()
    return redirect('../../accountview/'+str(id))
def accountreject(request,id):
    # if request.method == "post":
    reject = "Rejected"
    account = Account.objects.get(id=id)
    account.Apply_status = reject
    account.save()
    return redirect('../../accountview/'+str(id))
def accountpending(request,id):
    # if request.method == "post":
    pending = "Pending"
    account = Account.objects.get(id=id)
    account.Apply_status = pending
    account.save()
    return redirect('../../accountview/'+str(id))


def appliedaccountview(request):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Account.objects.filter(Apply_status="Applied")
        temp = loader.get_template('appliedaccountcard.html')
        context = {
            "account":account,
            "create_user" : current_user
        }
        
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')

def acceptaccountview(request):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Account.objects.filter(Apply_status="Accepted")
        temp = loader.get_template('acceptaccountview.html')
        context = {
            "account":account,
            "create_user" : current_user
        }
        
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')
def selectedaccountview(request):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Account.objects.filter(Apply_status="Selected")
        temp = loader.get_template('selectedaccount.html')
        context = {
            "account":account,
            "create_user" : current_user
        }
        
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')

def rejectedaccountview(request):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Account.objects.filter(Apply_status="Rejected")
        temp = loader.get_template('rejectedaccount.html')
        context = {
            "account":account,
            "create_user" : current_user
        }
        
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')


def pendingaccountview(request):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Account.objects.filter(Apply_status="Pending")
        temp = loader.get_template('pendingaccount.html')
        context = {
            "account":account,
            "create_user" : current_user
        }
        
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')


##############################  Account Related END  ######################################


# AUTH USERS

def dashboarduser(request):
    if 'user' in request.session:
        current_user = request.session['user']
        users = Dashboarduser.objects.all().values() 
        temp = loader.get_template('dashboarduserlist.html')
        context = {
            "dashboarduser": users,
            "current_user" : current_user
        }
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')

def adduser(request):
    x = request.POST['user']
    y = request.POST['pass']
    z = request.POST['passagain']
    job = Dashboarduser(username=x,password=y,cnf_password=z)
    job.save()
    return HttpResponseRedirect(reverse('dashboarduser'))

def deleteuser(request,id):
    delt = Dashboarduser.objects.get(id=id)
    delt.delete()
    return HttpResponseRedirect(reverse('dashboarduser'))



def loginauth(request):
    # if request.method == "post":
        x = request.POST['username']
        y = request.POST['password']
        user = Dashboarduser.objects.filter(username=x,password=y)       
        if user:
            request.session['user'] = x
            # 60*5 = 300
            request.session.set_expiry(300)   
            print(user)
            return redirect('index')
        else:
            
            return HttpResponseRedirect(reverse('login'))

def dashlogout(request):
    try:
        del request.session['user']
    except:
        return redirect('login')
    return redirect('login')

    # return HttpResponse(temp.render(context,request))
    
    # return render(request,'dashboardlogin.html')
    # return redirect('index')
    # return HttpResponse("Hello World")





    