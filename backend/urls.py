
from rest_framework.routers import DefaultRouter
# from rest_framework import routers
from .views import AccountViewset
from .views import CareerViewset
from .views import PasscodeViewset
from .views import AccountopeningViewset
from .views import CollegeViewset
from .views import DashboardViewset
from .views import VoucherViewset
from . import views
from django.urls import path ,include


router = DefaultRouter()
router.register('College',CollegeViewset)
router.register('Career',CareerViewset)
router.register('Accountopening',AccountopeningViewset)
router.register('Passcode',PasscodeViewset)
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
    path('jobs/', views.jobs,name="jobs"),
    path('jobs/addjob/', views.addjob,name="addjob"),
    path('totalaccount/', views.totalaccount,name="totalaccount"),
    path('voucher/', views.voucher,name="voucher"),
    path('voucher/addvoucher/', views.addvoucher,name="addvoucher"),
    path('voucher/deletevoucher/<int:id>', views.deletevoucher,name="deletevoucher"),
    path('voucher/updatevoucher/<int:id>', views.updatevoucher,name="updatevoucher"),
    path('voucher/updatevoucher/updatevoucherrecord/<int:id>', views.updatevoucherrecord,name="updatevoucherrecord"),
    path('totalaccount/accountview/<int:id>', views.accountview,name="accountview"),
    path('totalaccount/accountview/accept/<int:id>', views.accountaccept,name="accountaccept"),
    path('totalaccount/accountview/reject/<int:id>', views.accountreject,name="accountreject"),
    path('totalaccount/accountview/pending/<int:id>', views.accountpending,name="accountpending"),
    path('colleges/addcollege/', views.addcollege,name="addcollege"),
    path('colleges/deletecollege/<int:id>', views.deletecollege,name="deletecollege"),
    path('colleges/updatecollege/<int:id>', views.updatecollege,name="updatecollege"),
    path('colleges/updatecollege/updatecollegerecord/<int:id>', views.updatecollegerecord,name="updatecollegerecord"),

    path('passcode/addpasscode/', views.addpasscode,name="addpasscode"),
    path('passcode/deletepasscode/<int:id>', views.deletepasscode,name="deletepasscode"),
    path('jobs/deletejob/<int:id>', views.deletejob,name="deletejob"),


    # card
    path('appliedaccountview/', views.appliedaccountview,name="appliedaccountview"),
    path('acceptaccountview/', views.acceptaccountview,name="acceptaccountview"),
    path('selectedaccountview/', views.selectedaccountview,name="selectedaccountview"),
    path('rejectedaccountview/', views.rejectedaccountview,name="rejectedaccountview"),
    path('pendingaccountview/', views.pendingaccountview,name="pendingaccountview"),

    
   
]   
