
from rest_framework.routers import DefaultRouter
# from rest_framework import routers
from .views import AccountViewset
from .views import CareerViewset
from .views import PasscodeViewset
from .views import AccountopeningViewset
from .views import CollegeViewset
from .views import DashboardViewset
from .views import VoucherViewset
from .views import PasskeyViewset

from . import views
from django.urls import path ,include


router = DefaultRouter()
router.register('College',CollegeViewset)
router.register('Career',CareerViewset)
router.register('Accountopening',AccountopeningViewset)
router.register('Passcode',PasscodeViewset)
router.register('Passkey',PasskeyViewset)
router.register('Account',AccountViewset)
router.register('Dashboarduser',DashboardViewset)
router.register('Voucher',VoucherViewset)


urlpatterns = [
    path('', views.index,name="index"),
    path('login/loginauth/',views.loginauth,name="loginauth"),
    path('dashlogout/',views.dashlogout,name="dashlogout"),

    ###################------Login--------###########################
    path('login/', views.login,name="login"),
    path('dashboarduser/', views.dashboarduser,name="dashboarduser"),
    path('dashboarduser/adduser/', views.adduser,name="adduser"),
    path('dashboarduser/deleteuser/<int:id>', views.deleteuser,name="deleteuser"),
    

    ###############-------End Login-------##################

    # API
    path('register/', include(router.urls)),

    # PAGES
    path('index/', views.index,name="index"),
    path('colleges/', views.colleges,name="colleges"),
    path('passcode/', views.passcode,name="passcode"),
    path('passkey/', views.passkey,name="passkey"),
    path('jobs/', views.jobs,name="jobs"),
    path('jobs/addjob/', views.addjob,name="addjob"),
    path('totalaccount/', views.totalaccount,name="totalaccount"),
    path('voucher/', views.voucher,name="voucher"),
    path('voucher/addvoucher/', views.addvoucher,name="addvoucher"),
    path('voucher/deletevoucher/<int:id>', views.deletevoucher,name="deletevoucher"),
    path('voucher/updatevoucher/<int:id>', views.updatevoucher,name="updatevoucher"),
    path('voucher/updatevoucher/updatevoucherrecord/<int:id>', views.updatevoucherrecord,name="updatevoucherrecord"),
    
    path('totalaccount/accountview/<int:id>', views.accountview,name="accountview"),
    path('totalaccount/accountview/reject/<int:id>', views.accountreject,name="accountreject"),
    path('totalaccount/accountview/pending/<int:id>', views.accountpending,name="accountpending"),
    path('totalaccount/accountview/accept/<int:id>', views.accountaccept,name="accountaccept"),
   
    path('totalinternship/accountview/select/<int:id>', views.accountselect,name="accountselect"),
    path('totalinternship/accountview/reject/<int:id>', views.accountreject,name="accountreject"),
    path('totalinternship/accountview/pending/<int:id>', views.accountpending,name="accountpending"),
    path('rejectedinternshipview/accountview/<int:id>', views.accountview,name="accountview"),
    path('selectedinternshipview/accountview/<int:id>', views.accountview,name="accountview"),
    path('pendinginternshipview/accountview/<int:id>', views.accountview,name="accountview"),

    path('colleges/addcollege/', views.addcollege,name="addcollege"),
    path('colleges/deletecollege/<int:id>', views.deletecollege,name="deletecollege"),
    path('colleges/updatecollege/<int:id>', views.updatecollege,name="updatecollege"),
    path('colleges/updatecollege/updatecollegerecord/<int:id>', views.updatecollegerecord,name="updatecollegerecord"),

    path('passcode/addpasscode/', views.addpasscode,name="addpasscode"),
    path('passcode/deletepasscode/<int:id>', views.deletepasscode,name="deletepasscode"),

    path('passkey/addpasskey/', views.addpasskey,name="addpasskey"),
    path('passkey/activekey/<int:id>', views.activekey,name="activekey"),
    path('passkey/inactivekey/<int:id>', views.inactivekey,name="inactivekey"),
    path('passkey/deletepasskey/<int:id>', views.deletepasskey,name="deletepasskey"),
#Internship 
    path('internship/', views.internship,name="internship"),

# End Entership
    path('fresher/', views.fresher,name="fresher"),
    path('experience/', views.experience,name="experience"),

    path('jobs/deletejob/<int:id>', views.deletejob,name="deletejob"),
    path('jobs/jobview/updatedisplay/<int:id>', views.updatedisplay,name="updatedisplay"),
    path('jobs/jobview/<int:id>', views.jobview,name="jobview"),
    
    path('totalfresher/', views.totalfresher,name="totalfresher"),
    path('totalfresher/accountview/<int:id>', views.accountview,name="accountview"),
    path('rejectedfresherview/accountview/<int:id>', views.accountview,name="accountview"), 
    path('selectedfresherview/', views.selectedfresherview,name="selectedfresherview"),
    path('selectedfresherview/accountview/<int:id>', views.accountview,name="accountview"),
    path('rejectedfresherview/', views.rejectedfresherview,name="rejectedfresherview"),
    path('rejectedfresherview/accountview/<int:id>', views.accountview,name="accountview"),
    path('pendingfresherview/', views.pendingfresherview,name="pendingfresherview"),
    path('pendingfresherview/accountview/<int:id>', views.accountview,name="accountview"),
    path('totalfresher/accountview/select/<int:id>', views.accountselect,name="accountselect"),
    path('totalfresher/accountview/accept/<int:id>', views.accountaccept,name="accountaccept"),
    path('totalfresher/accountview/reject/<int:id>', views.accountreject,name="accountreject"),
    path('totalfresher/accountview/pending/<int:id>', views.accountpending,name="accountpending"),


    path('totalinternship/', views.totalinternship,name="totalinternship"),
    path('totalinternship/accountview/<int:id>', views.accountview,name="accountview"),
    path('selectedinternshipview/', views.selectedinternshipview,name="selectedinternshipview"),
    path('selectedinternshipview/accountview/<int:id>', views.accountview,name="accountview"),
    path('rejectedinternshipview/', views.rejectedinternshipview,name="rejectedinternshipview"),
    path('rejectedinternshipview/accountview/<int:id>', views.accountview,name="accountview"),
    path('pendinginternshipview/', views.pendinginternshipview,name="pendinginternshipview"),
    path('pendinginternshipview/accountview/<int:id>', views.accountview,name="accountview"),
    path('totalinternship/accountview/select/<int:id>', views.accountselect,name="accountselect"),
    path('totalinternship/accountview/accept/<int:id>', views.accountaccept,name="accountaccept"),
    path('totalinternship/accountview/reject/<int:id>', views.accountreject,name="accountreject"),
    path('totalinternship/accountview/pending/<int:id>', views.accountpending,name="accountpending"),

    path('totalexperience/', views.totalexperience,name="totalexperience"),
    path('totalexperience/accountview/<int:id>', views.accountview,name="accountview"),
    path('selectedexperienceview/', views.selectedexperienceview,name="selectedexperienceview"),
    path('selectedexperienceview/accountview/<int:id>', views.accountview,name="accountview"),
    path('rejectedexperienceview/', views.rejectedexperienceview,name="rejectedexperienceview"),
    path('rejectedexperienceview/accountview/<int:id>', views.accountview,name="accountview"),
    path('pendingexperienceview/', views.pendingexperienceview,name="pendingexperienceview"),
    path('pendingexperienceview/accountview/<int:id>', views.accountview,name="accountview"),
    path('totalexperience/accountview/select/<int:id>', views.accountselect,name="accountselect"),
    path('totalexperience/accountview/accept/<int:id>', views.accountaccept,name="accountaccept"),
    path('totalexperience/accountview/reject/<int:id>', views.accountreject,name="accountreject"),
    path('totalexperience/accountview/pending/<int:id>', views.accountpending,name="accountpending"),

#  bda 
    path('bdainternship/', views.bdainternship,name="bdainternship"),
    path('totalbdainternship/', views.totalbdainternship,name="totalbdainternship"),
    path('totalbdainternship/accountview/<int:id>', views.accountview,name="accountview"),
    path('selectedbdainternshipview/', views.selectedbdainternshipview,name="selectedbdainternshipview"),
    path('selectedbdainternshipview/accountview/<int:id>', views.accountview,name="accountview"),
    path('rejectedbdainternshipview/', views.rejectedbdainternshipview,name="rejectedbdainternshipview"),
    path('rejectedbdainternshipview/accountview/<int:id>', views.accountview,name="accountview"),
    path('pendingbdainternshipview/', views.pendingbdainternshipview,name="pendingbdainternshipview"),
    path('pendingbdainternshipview/accountview/<int:id>', views.accountview,name="accountview"),
    path('totalbdainternship/accountview/select/<int:id>', views.accountselect,name="accountselect"),
    path('totalbdainternship/accountview/accept/<int:id>', views.accountaccept,name="accountaccept"),
    path('totalbdainternship/accountview/reject/<int:id>', views.accountreject,name="accountreject"),
    path('totalbdainternship/accountview/pending/<int:id>', views.accountpending,name="accountpending"),
   
   
   
    path('bdafresher/', views.bdafresher,name="bdafresher"),
    path('totalbdafresher/', views.totalbdafresher,name="totalbdafresher"),
    path('totalbdafresher/accountview/<int:id>', views.accountview,name="accountview"),
    path('selectedbdafresherview/accountview/<int:id>', views.accountview,name="accountview"),
    path('selectedbdafresherview/', views.selectedbdafresherview,name="selectedbdafresherview"),
    path('rejectedbdafresherview/accountview/<int:id>', views.accountview,name="accountview"),
    path('rejectedbdafresherview/', views.rejectedbdafresherview,name="rejectedbdafresherview"),
    path('pendingbdafresherview/accountview/<int:id>', views.accountview,name="accountview"),
    path('pendingbdafresherview/', views.pendingbdafresherview,name="pendingbdafresherview"),
    path('totalbdafresher/accountview/select/<int:id>', views.accountselect,name="accountselect"),
    path('totalbdafresher/accountview/accept/<int:id>', views.accountaccept,name="accountaccept"),
    path('totalbdafresher/accountview/reject/<int:id>', views.accountreject,name="accountreject"),
    path('totalbdafresher/accountview/pending/<int:id>', views.accountpending,name="accountpending"),
   
   
    path('bdaexperience/', views.bdaexperience,name="bdaexperience"),
    path('totalbdaexperience/', views.totalbdaexperience,name="totalbdaexperience"),
    path('totalbdaexperience/accountview/<int:id>', views.accountview,name="accountview"),
    path('selectedbdaexperienceview/accountview/<int:id>', views.accountview,name="accountview"),
    path('selectedbdaexperienceview/', views.selectedbdaexperienceview,name="selectedbdaexperienceview"),
    path('rejectedbdaexperienceview/accountview/<int:id>', views.accountview,name="accountview"),
    path('rejectedbdaexperienceview/', views.rejectedbdaexperienceview,name="rejectedbdaexperienceview"),
    path('pendingbdaexperienceview/accountview/<int:id>', views.accountview,name="accountview"),
    path('pendingbdaexperienceview/', views.pendingbdaexperienceview,name="pendingbdaexperienceview"),
    path('totalbdaexperience/accountview/select/<int:id>', views.accountselect,name="accountselect"),
    path('totalbdaexperience/accountview/accept/<int:id>', views.accountaccept,name="accountaccept"),
    path('totalbdaexperience/accountview/reject/<int:id>', views.accountreject,name="accountreject"),
    path('totalbdaexperience/accountview/pending/<int:id>', views.accountpending,name="accountpending"),
   

    path('bdaexperience/', views.bdaexperience,name="bdaexperience"),
    path('totalbdaexperience/', views.totalbdaexperience,name="totalbdaexperience"),
    path('selectedbdaexperienceview/', views.selectedbdaexperienceview,name="selectedbdaexperienceview"),
    path('rejectedbdaexperienceview/', views.rejectedbdaexperienceview,name="rejectedbdaexperienceview"),
    path('pendingbdaexperienceview/', views.pendingbdaexperienceview,name="pendingbdaexperienceview"),

    # card
    path('appliedaccountview/', views.appliedaccountview,name="appliedaccountview"),
    path('acceptaccountview/', views.acceptaccountview,name="acceptaccountview"),
    # path('selectaccountview/', views.selectaccountview,name="selectaccountview"),
    path('selectedaccountview/', views.selectedaccountview,name="selectedaccountview"),
    path('rejectedaccountview/', views.rejectedaccountview,name="rejectedaccountview"),
    path('pendingaccountview/', views.pendingaccountview,name="pendingaccountview"),

    
   
]   
