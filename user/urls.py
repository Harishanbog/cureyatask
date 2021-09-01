from django.urls import path
from .views import home,doctor,mobile_otp_verification,login,logout

app_name='user'
urlpatterns=[
    path('',home,name="home"),
    path('doctor/',doctor,name="doctor"),
    path('mobile_otp_verification/<slug>/',mobile_otp_verification,name="mobile_otp_verification"),
    path('login/',login,name="login"),
    path('logout/',logout,name="logout"),
]