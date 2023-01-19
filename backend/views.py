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
from .models import Passkey
from django.template import loader
from .serializers import AccountSerializer
from .serializers import CareerSerializer
from .serializers import PasscodeSerializer
from .serializers import AccountopeningSerializer
from .serializers import CollegeSerializer
from .serializers import DashboardSerializer
from .serializers import VoucherSerializer
from .serializers import PasskeySerializer
import datetime
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

import json

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

class PasskeyViewset(ModelViewSet):
    serializer_class= PasskeySerializer
    queryset = Passkey.objects.all()

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
        
        internship =Account.objects.filter(job_type="internship")
        fresher = Account.objects.filter(job_type="Fresher")
        experience = Account.objects.filter(job_type="experience")

        account = Account.objects.all().values()
        applied = Account.objects.filter(Apply_status="Applied")
        accept = Account.objects.filter(Apply_status="Accepted")
        reject = Account.objects.filter(Apply_status="Rejected")
        select = Account.objects.filter(Apply_status="Selected")
        pending = Account.objects.filter(Apply_status="Pending")
        amount_paid = Account.objects.filter(payment_status="success")
        amount_to_paid = Account.objects.filter(payment_status="Null")
        today = Account.objects.filter(created_at=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").split(" ")[0])
        
        # month = []
        # m = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").split(" ")[0])
        # mon = m[:7]
        # for acnt in account:
        #     if str([:7 acnt['created_at']) == mon:
        #         month.append(acnt) 

        tdy = len(list(today))
        # mnt = len(month)

        no_internship = len(list(internship))
        no_fresher = len(list(fresher))
        no_experience = len(list(experience))
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
            "internship": no_internship,
            "fresher": no_fresher,
            "experience":no_experience,
            "total" : totalaccount,
            "applied": no_applied,
            "accept": no_accept,
            "reject": no_reject,
            "select": no_select,
            "pending": no_pending,
            "paid":paid,
            "tobepaid":tobepaid,
            "current_user":current_user,
            "today":tdy,
            # "month":mnt
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
    
    passcode = Passcode(code=x, code_type=y)
    passcode.save()
    return HttpResponseRedirect(reverse('passcode'))

def deletepasscode(request,id):
    delt = Passcode.objects.get(id=id)
    delt.delete()
    return HttpResponseRedirect(reverse('passcode'))


def passkey(request):
    if 'user' in request.session:

        current_user = request.session['user']
        passkey = Passkey.objects.all().values()
        temp = loader.get_template('passkey.html')
        context = {
            "passkey" : passkey,
            "current_user": current_user
        }
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')


def addpasskey(request):

    x = request.POST['passkey']
    y = request.POST['status']
    z = Passkey.objects.filter(passkey=x)
    if z:
        return HttpResponseRedirect(reverse('passkey'))
    else:        
        passkey = Passkey(passkey=x, Apply_status=y)
        passkey.save()
        return HttpResponseRedirect(reverse('passkey'))

def deletepasskey(request,id):
    delt = Passkey.objects.get(id=id)
    delt.delete()
    return HttpResponseRedirect(reverse('passkey'))


def inactivekey(request,id):
    # if request.method == "post":
    inactive = "Inactive"
    passkey = Passkey.objects.get(id=id)
    passkey.Apply_status = inactive
    passkey.save()
    return redirect('../../passkey/')


def activekey(request,id):
    # if request.method == "post":
    active = "Active"
    passkey = Passkey.objects.get(id=id)
    passkey.Apply_status = active
    passkey.save()
    return redirect('../../passkey/')

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
    z = request.POST['collegestate']
    college = College(college_name=x, Apply_status=y,college_state=z)
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
        temp = loader.get_template('git ')
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
    z = request.POST['code']
    a = request.POST['description']
    b = request.POST['display']
    job = Opening(job=x,job_type=y,code=z,description=a,display=b)
    passcode = Passcode(code=z,code_type=x)
    passcode.save()
    job.save()
    return HttpResponseRedirect(reverse('jobs'))

def updatedisplay(request,id):
    x = "yes"
    y = "no"
    updatedisplay = Opening.objects.get(id=id)
    if updatedisplay.display == x:
        updatedisplay.display == y
        updatedisplay.save()
        return redirect('../../jobview/'+str(id))
    else:
        updatedisplay.display == x
        updatedisplay.save()
        return redirect('../../jobview/'+str(id))


def deletejob(request,id):
    delt = Opening.objects.get(id=id)
    delt.delete()
    return HttpResponseRedirect(reverse('jobs'))



def jobview(request,id):
    if 'user' in request.session:
        current_user = request.session['user']
        job = Opening.objects.get(id=id)
        temp = loader.get_template('jobviews.html')
        context = {
            "job":job,
            "create_user" : current_user
        }
        
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')
####################### Internship ##########################################

def internship(request):
    if 'user' in request.session:
        
        current_user = request.session['user']
        # job = Opening.objects.all().values()
        account = Account.objects.all().values()
        internship =Account.objects.filter(job_type="internship")
        internship_selected =Account.objects.filter(job_type="internship",Apply_status="Selected")
        internship_rejected =Account.objects.filter(job_type="internship",Apply_status="Rejected")
        internship_pending =Account.objects.filter(job_type="internship",Apply_status="Pending")

        no_internship = len(list(internship))
        no_internship_selected = len(list(internship_selected))
        no_internship_rejected = len(list(internship_rejected))
        no_internship_pending = len(list(internship_pending))
        context = {
            # "jobs" : job,
            "current_user": current_user,
            "internship": no_internship,
            "internship_selected": no_internship_selected,
            "internship_rejected": no_internship_rejected,
            "internship_pending": no_internship_pending,
    

        }
        temp = loader.get_template('internship.html')

        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')

def totalinternship(request):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Account.objects.all().values() 
        temp = loader.get_template('totalinternship.html')
        context = {
            "current_user":current_user,
            "accounts": account
        }
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')


def selectedinternshipview(request):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Account.objects.filter(job_type="Internship",Apply_status="Selected")
        temp = loader.get_template('selectedinternship.html')
        context = {
            "account":account,
            "create_user" : current_user
        }
        
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')
def rejectedinternshipview(request):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Account.objects.filter(job_type="Internship",Apply_status="Rejected")
        temp = loader.get_template('rejectedinternship.html')
        context = {
            "account":account,
            "create_user" : current_user
        }
        
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')
def pendinginternshipview(request):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Account.objects.filter(job_type="Internship",Apply_status="Pending")
        temp = loader.get_template('pendinginternship.html')
        context = {
            "account":account,
            "create_user" : current_user
        }
        
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')

####################### End Internship ##########################################
def fresher(request):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Account.objects.all().values()
        fresher =Account.objects.filter(job_type="fresher")
        fresher_selected =Account.objects.filter(job_type="fresher",Apply_status="Selected")
        fresher_rejected =Account.objects.filter(job_type="fresher",Apply_status="Rejected")
        fresher_pending =Account.objects.filter(job_type="fresher",Apply_status="Pending")
        no_fresher = len(list(fresher))
        no_fresher_selected = len(list(fresher_selected))
        no_fresher_rejected = len(list(fresher_rejected))
        no_fresher_pending = len(list(fresher_pending))
        context = {
            "account" : account,
            "current_user" : current_user,
            "fresher": no_fresher,
            "fresher_selected": no_fresher_selected,
            "fresher_rejected": no_fresher_rejected,
            "fresher_pending": no_fresher_pending,
        }
        temp = loader.get_template('fresher.html')
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')

def totalfresher(request):
    if 'user' in request.session:
        current_user = request.session['user']
        accounts = Account.objects.all().values() 
        temp = loader.get_template('totalfresher.html')
        context = {
            "current_user":current_user,
            "account": accounts
        }
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')

def selectedfresherview(request):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Account.objects.filter(job_type="fresher",Apply_status="Selected")
        temp = loader.get_template('selectedfresher.html')
        context = {
            "account":account,
            "create_user" : current_user
        }
        
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')

def rejectedfresherview(request):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Account.objects.filter(job_type="fresher",Apply_status="Rejected")
        temp = loader.get_template('rejectedfresher.html')
        context = {
            "account":account,
            "create_user" : current_user
        }
        
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')
def pendingfresherview(request):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Account.objects.filter(job_type="fresher",Apply_status="Pending")
        temp = loader.get_template('pendingfresher.html')
        context = {
            "account":account,
            "create_user" : current_user
        }
        
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')
def experience(request):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Account.objects.all().values()
        experience =Account.objects.filter(job_type="experience")
        experience_selected =Account.objects.filter(job_type="experience",Apply_status="Selected")
        experience_rejected =Account.objects.filter(job_type="experience",Apply_status="Rejected")
        experience_pending =Account.objects.filter(job_type="experience",Apply_status="Pending")
        no_experience= len(list(experience))
        no_experience_selected = len(list(experience_selected))
        no_experience_rejected = len(list(experience_rejected))
        no_experience_pending = len(list(experience_pending))
        context = {
            "account" : account,
            "current_user" : current_user,
            "experience": no_experience,
            "experience_selected": no_experience_selected,
            "experience_rejected": no_experience_rejected,
            "experience_pending": no_experience_pending,
        }
        temp = loader.get_template('experience.html')

        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')


def totalexperience(request):
    if 'user' in request.session:
        current_user = request.session['user']
        accounts = Account.objects.all().values() 
        temp = loader.get_template('totalexperience.html')
        context = {
            "current_user":current_user,
            "accounts": accounts
        }
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')

def selectedexperienceview(request):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Account.objects.filter(job_type="experience",Apply_status="Selected")
        temp = loader.get_template('selectedexperience.html')
        context = {
            "account":account,
            "create_user" : current_user
        }
        
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')

def rejectedexperienceview(request):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Account.objects.filter(job_type="experience",Apply_status="Rejected")
        temp = loader.get_template('rejectedexperience.html')
        context = {
            "account":account,
            "create_user" : current_user
        }
        
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')
def pendingexperienceview(request):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Account.objects.filter(job_type="experience",Apply_status="Pending")
        temp = loader.get_template('pendingexperience.html')
        context = {
            "account":account,
            "create_user" : current_user
        }
        
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')





####################### End Job ##########################################
####################### BDA DATA ##########################################
def bdainternship(request):
    if 'user' in request.session:
        
        current_user = request.session['user']
        # job = Opening.objects.all().values()
        account = Account.objects.all().values()
        bdainternship =Account.objects.filter(job_type="internship",job_name="Buisness Development Associate")
        bdainternship_selected =Account.objects.filter(job_type="internship",job_name="Buisness Development Associate",Apply_status="Selected")
        bdainternship_rejected =Account.objects.filter(job_type="internship",job_name="Buisness Development Associate",Apply_status="Rejected")
        bdainternship_pending =Account.objects.filter(job_type="internship",job_name="Buisness Development Associate",Apply_status="Pending")

        no_bdainternship = len(list(bdainternship))
        no_bdainternship_selected = len(list(bdainternship_selected))
        no_bdainternship_rejected = len(list(bdainternship_rejected))
        no_bdainternship_pending = len(list(bdainternship_pending))
        context = {
            # "jobs" : job,
            "current_user": current_user,
            "bda_internship": no_bdainternship,
            "bdainternship_selected": no_bdainternship_selected,
            "bdainternship_rejected": no_bdainternship_rejected,
            "bdainternship_pending": no_bdainternship_pending,
    

        }
        temp = loader.get_template('bdainternship.html')

        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')

def totalbdainternship(request):
    if 'user' in request.session:
        current_user = request.session['user']
        accounts = Account.objects.all().values() 
        temp = loader.get_template('totalbdainternship.html')
        context = {
            "current_user":current_user,
            "accounts": accounts
        }
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')
def selectedbdainternshipview(request):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Account.objects.filter(job_type="Internship",job_name="Buisness Development Associate",Apply_status="Selected")
        temp = loader.get_template('selectedbdainternship.html')
        context = {
            "account":account,
            "create_user" : current_user
        }
        
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')
def rejectedbdainternshipview(request):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Account.objects.filter(job_type="Internship",job_name="Buisness Development Associate",Apply_status="Rejected")
        temp = loader.get_template('rejectedbdainternship.html')
        context = {
            "account":account,
            "create_user" : current_user
        }
        
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')

def pendingbdainternshipview(request):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Account.objects.filter(job_type="Internship",job_name="Buisness Development Associate",Apply_status="Pending")
        temp = loader.get_template('pendingbdainternship.html')
        context = {
            "account":account,
            "create_user" : current_user
        }
        
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')

def bdafresher(request):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Account.objects.all().values()
        bdafresher =Account.objects.filter(job_type="fresher",job_name="Buisness Development Associate")
        bdafresher_selected =Account.objects.filter(job_type="fresher",Apply_status="Selected",job_name="Buisness Development Associate")
        bdafresher_rejected =Account.objects.filter(job_type="fresher",Apply_status="Rejected",job_name="Buisness Development Associate")
        bdafresher_pending =Account.objects.filter(job_type="fresher",Apply_status="Pending",job_name="Buisness Development Associate")
        no_bdafresher = len(list(bdafresher))
        no_bdafresher_selected = len(list(bdafresher_selected))
        no_bdafresher_rejected = len(list(bdafresher_rejected))
        no_bdafresher_pending = len(list(bdafresher_pending))
        context = {
            "account" : account,
            "current_user" : current_user,
            "bda_fresher": no_bdafresher,
            "bdafresher_selected": no_bdafresher_selected,
            "bdafresher_rejected": no_bdafresher_rejected,
            "bdafresher_pending": no_bdafresher_pending,
        }
        temp = loader.get_template('bdafresher.html')
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')


def totalbdafresher(request):
    if 'user' in request.session:
        current_user = request.session['user']
        accounts = Account.objects.all().values() 
        temp = loader.get_template('totalbdafresher.html')
        context = {
            "current_user":current_user,
            "account": accounts
        }
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')

def selectedbdafresherview(request):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Account.objects.filter(job_type="fresher",job_name="Buisness Development Associate",Apply_status="Selected")
        temp = loader.get_template('selectedbdafresher.html')
        context = {
            "account":account,
            "create_user" : current_user
        }
        
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')

def rejectedbdafresherview(request):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Account.objects.filter(job_type="fresher",job_name="Buisness Development Associate",Apply_status="Rejected")
        temp = loader.get_template('rejectedbdafresher.html')
        context = {
            "account":account,
            "create_user" : current_user
        }
        
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')
def pendingbdafresherview(request):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Account.objects.filter(job_type="fresher",job_name="Buisness Development Associate",Apply_status="Pending")
        temp = loader.get_template('pendingbdafresher.html')
        context = {
            "account":account,
            "create_user" : current_user
        }
        
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')

# bda experienced data ##
def bdaexperience(request):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Account.objects.all().values()
        bdaexperience =Account.objects.filter(job_type="experience",job_name="Buisness Development Associate")
        bdaexperience_selected =Account.objects.filter(job_type="experience",job_name="Buisness Development Associate",Apply_status="Selected")
        bdaexperience_rejected =Account.objects.filter(job_type="experience",job_name="Buisness Development Associate",Apply_status="Rejected")
        bdaexperience_pending =Account.objects.filter(job_type="experience",job_name="Buisness Development Associate",Apply_status="Pending")
        no_bdaexperience= len(list(bdaexperience))
        no_bdaexperience_selected = len(list(bdaexperience_selected))
        no_bdaexperience_rejected = len(list(bdaexperience_rejected))
        no_bdaexperience_pending = len(list(bdaexperience_pending))
        context = {
            "account" : account,
            "current_user" : current_user,
            "bda_experience": no_bdaexperience,
            "bdaexperience_selected": no_bdaexperience_selected,
            "bdaexperience_rejected": no_bdaexperience_rejected,
            "bdaexperience_pending": no_bdaexperience_pending,
        }
        temp = loader.get_template('bdaexperience.html')

        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')

def totalbdaexperience(request):
    if 'user' in request.session:
        current_user = request.session['user']
        accounts = Account.objects.all().values() 
        temp = loader.get_template('totalbdaexperience.html')
        context = {
            "current_user":current_user,
            "accounts": accounts
        }
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')
def selectedbdaexperienceview(request):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Account.objects.filter(job_type="experience",job_name="Buisness Development Associate",Apply_status="Selected")
        temp = loader.get_template('selectedbdaexperience.html')
        context = {
            "account":account,
            "create_user" : current_user
        }
        
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')
def rejectedbdaexperienceview(request):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Account.objects.filter(job_type="experience",job_name="Buisness Development Associate",Apply_status="Rejected")
        temp = loader.get_template('rejectedbdaexperience.html')
        context = {
            "account":account,
            "create_user" : current_user
        }
        
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')
def pendingbdaexperienceview(request):
    if 'user' in request.session:
        current_user = request.session['user']
        account = Account.objects.filter(job_type="experience",job_name="Buisness Development Associate",Apply_status="Pending")
        temp = loader.get_template('pendingbdaexperience.html')
        context = {
            "account":account,
            "create_user" : current_user
        }
        
        return HttpResponse(temp.render(context,request))
    else:
        return redirect('login')
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
def accountselect(request,id):
    # if request.method == "post":
    select = "Selected"
    account = Account.objects.get(id=id)
    account.Apply_status = select
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





    