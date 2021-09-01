from django.http.response import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404
from .models import userdetails
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.mail import send_mail
from twilio.rest import Client
import random

# Your Account SID from twilio.com/console
account_sid = "AC1b6527f684e9c359e3dcd87c2da597b8"
# Your Auth Token from twilio.com/console
auth_token  = "a9d6871b0e94268c9c73aa919e799e71"

client = Client(account_sid, auth_token)
# Create your views here.

def home(request):
    if request.method=='POST':
        if request.POST['type']=='doctortype':
               return render(request,"user/doctor.html")
        elif request.POST['type']=='patienttype':
            return render(request,"user/patient.html")   
             
    else:
        return render(request,"user/index.html") 

def doctor(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        number=request.POST['number']
        type=request.POST['type']
        mobile_otp=random.randint(100000,999999)
        email_otp=random.randint(1000,9999)
        if User.objects.filter(email=email).exists():
            messages.info(request,'Email Taken')
            return redirect("/registration")
        user=User.objects.create_user(username=email,first_name=firstname,last_name=lastname,email=email,password=password)
        user.save()
        user1=userdetails.objects.create(user=user,number=number,type=type,mobile_otp=mobile_otp,email_otp=email_otp)
        user1.randomid=random.sample(range(10000,99999),1)[0]
        user1.save()
        if type=='doctor':
            user.username="C1"+str(user1.randomid)
            user.save()
        elif type=='patient': 
            user.username="C2"+str(user1.randomid)
            user.save() 

        
        Mmess=f"Welcome to cureya Your otp is {mobile_otp} {email_otp}"
        Emess=f"Welcome to cureya Your otp is {email_otp}"
        send_mail('Welcome',Emess,'ss',[email],fail_silently=False)
        message = client.messages \
        .create(
            body=Mmess,
            from_='+17048692490',
            to=number
        ) 
        return render(request,"user/otp_verification.html",{'user':user,'mobile':False})
         

    

           
           
           
         
def mobile_otp_verification(request,slug):
    otp=request.POST['otp']
    user=User.objects.get(id=slug)
    getusr=userdetails.objects.get(user=slug)
    otptype=request.POST.get('otptype')
    if otptype=='mobile':
        if userdetails.objects.filter(user=user).last().mobile_otp==int(otp):
            messages.success(request,'Mobile number verified succesfully')
            print("yes")
            return render(request,"user/otp_verification.html",{'user':user,'mobile':True})
        else:
            messages.warning(request,'Wrong otp')
            return render(request,"user/otp_verification.html",{'user':user})

    elif otptype=='email':
        user=User.objects.get(id=slug)
        if userdetails.objects.filter(user=user).last().email_otp==int(otp):
            print(user.username)
            msg=f" User created successfully and Mobile number and email both were verified your username is:{user.username}"
            messages.success(request,'User id has been sent your email please use it to login')
            send_mail('Congratulations!',msg,'ss',['harishanbog7@gmail.com'],fail_silently=False)
            return redirect('/registration/login')
            
        else:
            messages.warning(request,'Wrong otp')
            return render(request,"user/otp_verification.html",{'user':user})

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            usr=User.objects.get(username=username)
        except:
            messages.info(request,'User doesnot exist please register')
            return redirect('/registration/login')    


        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponse("congratulations! you have successfully logged in")

        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/registration/login')    

    else:
        
        return render(request,'user/login.html')

def logout(request):
    auth.logout(request)      
    return redirect('/login')                    




 



    

 

