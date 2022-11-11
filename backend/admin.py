from django.contrib import admin
from .models import Account
from .models import Career
from .models import Passcode
from .models import Opening
from .models import College
from .models import Dashboarduser
from .models import Voucher
# Register your models here.
@admin.register(Account)
class Accountadmin(admin.ModelAdmin):
    list_display = [ 'id' , 'firstname' ,'lastname','email','password' ,'mobile_no' , 'whatsapp_no','gender','Date_of_birth','state','district','college_state','college','course','branch','passing_year','Apply_status','created_at','enrolment','payment_status']

@admin.register(Career)
class Careeradmin(admin.ModelAdmin):
    list_display = ['id','Name','Email','Apply_status']

@admin.register(Passcode)
class Passcodeadmin(admin.ModelAdmin):
    list_display = ['id','code','code_type','valid_date']
@admin.register(Opening)
class Accountopeningadmin(admin.ModelAdmin):
    list_display = ['id','job','job_type']
class Collegeadmin(admin.ModelAdmin):
    list_display = ['id','college_name','college_state','Apply_status']
@admin.register(Dashboarduser)
class Dashboarduseradmin(admin.ModelAdmin):
    list_display = ['id','username','password','cnf_password']

@admin.register(Voucher)
class Voucheradmin(admin.ModelAdmin):
    list_display = ['id','voucher_code','price','status']


