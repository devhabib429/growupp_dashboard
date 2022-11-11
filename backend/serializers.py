from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Account
from .models import Career
from .models import Passcode
from .models import Opening
from .models import College
from .models import Dashboarduser
from .models import Voucher
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model= Account
        fields =[ 'id' , 'firstname' ,'lastname','email','password' ,'mobile_no' , 'whatsapp_no','gender','Date_of_birth','state','district','college_state','college','course','branch','passing_year','Apply_status','created_at','enrolment','payment_status']

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Career
        fields =['id','Name','Email','Apply_status']

class PasscodeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Passcode
        fields =['id','code','code_type','valid_date']

class AccountopeningSerializer(serializers.ModelSerializer):
    class Meta:
        model= Opening
        fields =['id','job','job_type']

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model= College
        fields =['id','college_name','college_state','Apply_status']

class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model= Dashboarduser
        fields =['id','username','password','cnf_password']

class VoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model= Voucher
        fields =['id','voucher_code','price','status']