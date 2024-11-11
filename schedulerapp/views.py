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
from cloudapp.models import *
from userapp.models import *
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
import time

# Create your views here.


def scheduler_login(request):
    if request.method=='POST':
        name=request.POST.get('name')
        pwd=request.POST.get('pwd')
        if name=='scheduler' and pwd=='scheduler':
            messages.info(request,"login successfull")
            return redirect('scheduler_dashboard')
        else:
            messages.warning(request,'Something Wrong, Please try again.')
            return redirect ('scheduler_login')
    return render(request,'scheduler/scheduler-login.html')



def scheduler_dashboard(request):
    users=userModel.objects.count()
    uploads=fileModel.objects.count()
    requests=requestModel.objects.count()

    pendings=fileModel.objects.filter(status='Pending').count()
    pendings=fileModel.objects.filter(status='Assigned').count()
    vm=vmModel.objects.count()
    return render(request,'scheduler/scheduler-dashboard.html',{'users':users,'uploads':uploads,'requests':requests,'pendings':pendings,'vm':vm})




def scheduler_assign_task(request):
    app =vmModel.objects.all()
    data = fileModel.objects.all().order_by("-file_id")

    # user_id=request.session["user_id"]
    # filedetails = fileModel.objects.get(file_id= id)
    # owner_id=filedetails.owner_id
    # file_id=filedetails.file_id 
    # file_name = filedetails.file_name
    # file=filedetails.file
    # file_size = filedetails.file_size
    # file_type=filedetails.file_type
    # print(file_type)
    # file=filedetails.file
    # description=filedetails.description
    # print(description) 
    # requestModel.objects.create(file_name=file_name,file=file,file_size=file_size,user_id=user_id,owner_id=owner_id,description=description,file_type=file_type,file_id=file_id)
    # print('ddddddddddddddddddddd') 
    return render(request,'scheduler/scheduler-assign-task.html',{'data':data,'app':app})

def scheduler_task(request,id):
    
    user_id=request.session["user_id"]
    filedetails = fileModel.objects.get(file_id= id)
    file_id=filedetails.file_id 
    file_name = filedetails.file_name
    file=filedetails.file
    file_size = filedetails.file_size
    file_type=filedetails.file_type
    print(file_type)
    file=filedetails.file
    description=filedetails.description
    file_uploaded_date=filedetails.file_uploaded_date
    file_uploaded_time=filedetails.file_uploaded_time
    
    print(description) 

    now =datetime.now()
    print(now,'time success')

    time=now.strftime('%H:%M')
    print(time,'time success-2')
    
    vm_id=vmModel.objects.get(status='ON')
    print(vm_id)
   
    vm = vmModel.objects.get(vm_id=vm_id.vm_id)
    print(vm)

   
    if fileModel.objects.filter(file_id=id , status="Assigned"):
      
       messages.warning(request,"File Already Assigned")
       return redirect('scheduler_assign_task')
            
    else:

     requestModel.objects.create(file_name=file_name,file=file,file_size=file_size,user_id=user_id,description=description, file_type=file_type,file_id=file_id,vm_id=vm.vm_id,file_uploaded_date=file_uploaded_date,file_uploaded_time=file_uploaded_time,requested_time=time)
    print('ddddddddddddddddddddd') 

    # fileModel.objects.create(vm_id=vm.vm_id,)
    # print('created successfully vm id in filemodel')
    
    fileModel.objects.filter(file_id=id).update(status="Assigned")
   
    print("sravaniiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")


    request_id=requestModel.objects.get(file_id=id)
    file_uploaded_time=request_id.file_uploaded_time
    print(type(file_uploaded_time))

    tm=str(file_uploaded_time)
    print(tm)
    print("Chanuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
    requested_time=request_id.requested_time
    tm1=str(requested_time)
    print("success1111111111111111111111111111111111111111111111")
    print(tm1)



    t1 = datetime.strptime(tm1, '%H:%M')
    print(t1)
    print('yesssssssssssssssssssssssssssssssssssssssss')
    print("success")

    t2 = datetime.strptime(tm, '%H:%M')
    print(t1)
    print('yesssssssssssssssssssssssssssssssssssssssss')
    print("success2222222222222222222222")


    

    print(type(t1))

    t = t1 - t2
   
    print(t)
    print("success33333333333333333333333333333333333")

    time=  t

    timestr=str(time)
    print(timestr)
    print(type(timestr))

    print("okkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
    print(time)
    print("success44444444444444444444444444444444")
   

    obj = get_object_or_404(requestModel,file_id=id)
    print("success5555555555555555555555555555555555")
    if  time ==  time:
        print("ggggggggggggggggggggggggggggggg")
 

        obj.differenced_time = timestr[:4]
        print(type(obj.differenced_time))
        print(obj.differenced_time)
        print('success66666666666666666666666666666666')
        print(obj)
        print(obj.differenced_time)
        obj.save(update_fields=['differenced_time'])
        obj.save()
        print('finallysucesssssssssssssssssssssssssssssssssssssssssssssssssss')
        messages.info(request,'Task Assigned Successfully.')
       
    else:
        print("wrongggggggggggggggggggggggggggggggggggggggg")
        obj.differenced_time = time
        obj.save(update_fields=['differenced_time'])
        obj.save()
        print('success777777777777777777777777777777777777777')
    messages.info(request,'Task Assigned Successfully.')
    return redirect('scheduler_dashboard')
    return render(request,'scheduler/scheduler-assigned-task.html')
 


def scheduler_manage_vm_resourses(request):
   data = requestModel.objects.all().order_by("-request_id")
   return render(request,'scheduler/scheduler-manage-vm-resourses.html',{'data':data})



def scheduler_view_task(request):
   data = fileModel.objects.all().order_by("-file_id")
   return render(request,'scheduler/scheduler-view-task.html',{'data':data})

