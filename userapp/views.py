

from re import M
from django.shortcuts import render
from ast import Pass
from dataclasses import field
from tkinter.tix import COLUMN
from urllib import request
from email.headerregistry import Address
from unicodedata import name
from django.contrib import messages
from tabnanny import check
from django.shortcuts import render
from userapp.models import *
from cloudapp.models import *
from schedulerapp.models import *
from django.shortcuts import render,redirect,get_object_or_404

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.db.models import Q, F, Sum
import random
import requests
from cryptography.fernet import Fernet
from mainapp.check_internet import *
from datetime import datetime

# Create your views here.

ALLOWED_EXTENSIONS=set(['txt','py','html','java','js'])


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        password = request.POST.get('password')
        print(password)

        try:
            check = userModel.objects.get(email=email,password=password)
            print(check)
            request.session["user_id"] = check.user_id
            messages.info(request,"Login Successfully")
            return redirect('user_dashboard')
            
        
        except:
            messages.warning(request,"Invalid username or password")
            return redirect('user_login')


    return render(request,'user/user-login.html')


#user register
def user_register(request):
    if request.method=='POST' and request.FILES['user_image']:
        user_name=request.POST ['user_name']
        print(user_name) 
        email=request.POST['email']       
        password=request.POST['password']
        mobile=request.POST['mobile']
        dob=request.POST['dob']
        location=request.POST['location']
        user_image=request.FILES['user_image']


        if userModel.objects.filter(email=email).filter(verification = "verified"):
            messages.warning(request,"Email  Already  Exists!")
            print("Already")
        elif userModel.objects.filter(email=email).filter(verification = "Pending"):
            messages.warning(request,"Already Rejistered, Just verify your account!")
            otp=random.randint(2222,4444)
            userModel.objects.filter(email=email,verification='Pending').update(otp=otp)
            url = "https://www.fast2sms.com/dev/bulkV2"
            # create a dictionary
            my_data = {'sender_id': 'FSTSMS', 
                        'message': 'Welcome to Dual Access Control in Cloud, your verification OPT is '+str(otp)+'Thanks for request of OTP.', 
                        'language': 'english', 
                        'route': 'p', 
                        'numbers': mobile
            }

            # create a dictionary
            headers = {
                'authorization': 'D4vuFnk1sNQOl6SRpfZUT23ewPX0BoLrzAJVgqtW8bxyHEGjImfkE0NtULg1TG9xImYHpVZjQMnBSOoa',
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache"
            }
            
            if connect():

            # make a post request
                response = requests.request("POST",
                                            url,
                                            data = my_data,
                                            headers = headers)
            
                print(response.text)      
            return redirect('user_otp')  

        else:
            print("vssdvsdvsd")
            otp=random.randint(2222,4444)
            url = "https://www.fast2sms.com/dev/bulkV2"
            # create a dictionary
            my_data = {'sender_id': 'FSTSMS', 
                        'message': 'Welcome to CloudHost, your verification OPT is '+str(otp)+'Thanks for request of OTP.', 
                        'language': 'english', 
                        'route': 'p', 
                        'numbers': mobile
            }

            # create a dictionary
            headers = {
                'authorization': 'D4vuFnk1sNQOl6SRpfZUT23ewPX0BoLrzAJVgqtW8bxyHEGjImfkE0NtULg1TG9xImYHpVZjQMnBSOoa',
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache"
            }

            if connect():
            # make a post request
                response = requests.request("POST",
                                            url,
                                            data = my_data,
                                            headers = headers)
            
                print(response.text)        

            userModel.objects.create(user_name=user_name,password=password,mobile=mobile,email=email,dob=dob,location=location,user_image=user_image,otp=otp)
            messages.success(request,'Account Created Successfully!')
            return redirect('user_otp')
    return render(request,'user/user-register.html')

def user_otp(request):
    # user_id=request.session['user_id']

    if request.method == "POST":
        otp = request.POST.get('otp')
        print(otp)
        try:
            print('ppppppppppppppppppppp')
            check = userModel.objects.get(otp=otp)
            user_id = request.session['user_id']=check.user_id
            otp=check.otp
            print(otp)
            if otp == otp:
                userModel.objects.filter(user_id=user_id).update(verification='Verified')
                messages.info(request,'Account Created Successfully!')
                return redirect('user_login')
            else:
                return redirect('user_otp')
        except:
            pass
    return render(request,'user/user-otp.html')
        


def user_dashboard(request):
    user_id=request.session["user_id"]
    file=fileModel.objects.filter(user_id=user_id).values('file_id').count()
    storage=fileModel.objects.filter(user_id=user_id).aggregate(payment=Sum('file_size'))

    # uploads=fileModel.objects.count()
    vm=vmModel.objects.count()
    return render(request,'user/user-dashboard.html',{'file':file,'vm':vm,'payment':storage})
# 

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS 


def user_upload_files(request):
 
    if request.method=='POST' and 'file' in request.FILES:
        file = request.FILES['file']
        print(file)
        description = request.POST['description']
        print(description)
        file_name=file.name
        file_size=file.size
        file_type=file.content_type
        
        now =datetime.now()
        print(now,'time success')

        time=now.strftime('%H:%M')
        print(time,'time success-2')



        user_id=request.session["user_id"]
        vm_id=vmModel.objects.get(status='ON')
        vm=vmModel.objects.get(vm_id=vm_id.vm_id)
        status1=vm.status


        if not allowed_file(file_name):
            messages.warning(request,"Allowed File Types are: txt, html, py, java, js,")
            return redirect('user_upload_files')

        if fileModel.objects.filter(file_name=file_name) :
            messages.warning(request,"File Already Exists")
            return redirect('user_upload_files')
     
        else:
            # vm=vmModel.objects.get(status='ON')
            data_storage=fileModel.objects.create(file=file,file_name=file_name,file_size=file_size,file_type=file_type,user_id=user_id,description=description,status1=status1,vm_id=vm.vm_id,file_uploaded_time=time)
            data_storage.save()

        #File Encryption



        print('ggggggggggggggggggggggggggggggggggggggggggg')
        if data_storage:
             messages.info(request,"Uploaded Successfully")
             
             #     print(messages)
        else:
            messages.info(request,"Something Wrong, Please try again.")
    return render(request,'user/user-file-upload.html')



def user_view_files(request):
    user_id=request.session["user_id"]
    data = fileModel.objects.filter(user_id=user_id).order_by("-file_id")
    print(user_id)
    return render(request,'user/user-view-files.html',{'data':data})


  
def user_profile(request):
    user_id=request.session["user_id"]
    data = userModel.objects.get(user_id=user_id)
    obj = get_object_or_404(userModel,user_id=user_id)
    if request.method=='POST':
        print('ftttyy')
        user_name=request.POST['user_name']
        # user_image=request.POST['user_image']
        print(user_name)
        email=request.POST['email']
        mobile=request.POST['mobile']
        location=request.POST['location']
        dob = request.POST['dob']
        password = request.POST['password']
        print('ddddddddddddddddddddd')
        if len(request.FILES) != 0:
            print("ggggggggggggggggggggggggggggggg")
            user_image = request.FILES['user_image']
            obj.user_name = user_name
            obj.mobile = mobile
            obj.email = email
            obj.location =location
            obj.dob = dob
            obj.password = password
            obj.user_image = user_image
            print(type(obj.user_image))
            obj.save(update_fields=['user_name','mobile','email','location','user_image','dob','password'])
            obj.save()

   
        else:
            obj.user_name = user_name
            obj.mobile = mobile
            obj.email = email
            obj.location =location
            obj.dob = dob
            print(type(obj.dob))
            obj.password = password

            print(type(obj.password))
            obj.save(update_fields=['user_name','mobile','email','location','dob','password'])
            print("dddddddddddddddddddddddddddd")
            obj.save()
            messages.info(request,'Updated Successfully!')
    return render(request,'user/user-profile.html',{'data':data})
