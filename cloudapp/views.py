from turtle import down
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from userapp.models import *
from mainapp.models import *
from cloudapp.models import *
from schedulerapp.models import *
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
import requests
import random
import numpy as np
import matplotlib.pyplot as plt

from django.core.mail import EmailMultiAlternatives
from algorithm_project.settings import DEFAULT_FROM_EMAIL
from mainapp.check_internet import *
# from Power.settings import DEFAULT_FROM_EMAIL
# import pandas as pd

def cloud_login(request):
    if request.method=='POST':
        name=request.POST.get('name')
        pwd=request.POST.get('pwd')
        if name=='cloud' and pwd=='cloud':
            messages.info(request,"login successfull")
            return redirect('cloud_dashboard')
        else:
            messages.warning(request,'Something Wrong, Please try again.')
            print('message')
            return redirect ('cloud_login')
    return render(request,'main/cloud-login.html')



def cloud_dashboard(request):
    users=userModel.objects.count()
    uploads=fileModel.objects.count()
    requests=requestModel.objects.count()
    data1 = requestModel.objects.filter(vm_id=1).count()
    print(data1)
    data2 = requestModel.objects.filter(vm_id=2).count()
    print(data2)
    data3 = requestModel.objects.filter(vm_id=3).count()
    return render(request,'cloud/cloud-dashboard.html',{'users':users,'uploads':uploads,'requests':requests,'data1':data1,'data2':data2,'data3':data3})



def cloud_add_virtual_machine(request):
    print("fffffffffffffffffffffffffffffffff")
    if request.method=='POST':
        print("fffffffffffffffffffffffffffffffff")
        try:
            count=vmModel.objects.all().count()
            if count >= 3:
                messages.warning(request,"You can not add more than 3.")
                return redirect('cloud_add_virtual_machine')
        except:
            pass
        vm_name=request.POST['vm_name']
        print(vm_name)
        os=request.POST['os']
        print(os)
        storage_type=request.POST['storage_type']
        storage=request.POST['storage']
        cpu=request.POST['cpu']
        ram=request.POST['ram']

        vm = vmModel.objects.create(vm_name=vm_name,os=os,storage=storage,cpu=cpu,ram=ram,storage_type=storage_type)
        vm.save()
        messages.info(request,'Added Successfully.')
    return render(request,'cloud/cloud-add-virtual-machine.html')

def cloud_edit_virtual_machine(request,id):
    
    i = vmModel.objects.get(vm_id=id)
    if request.method=='POST':
        vm_name=request.POST['vm_name']
        os=request.POST['os']
        storage=request.POST['storage']        
        cpu=request.POST['cpu']
        ram=request.POST['ram']
        data = get_object_or_404(vmModel,vm_id=id)

        data.vm_name = vm_name
        data.storage = storage
        data.os = os
        data.cpu = cpu
        data.ram = ram
        data.save(update_fields=['vm_name','os','storage','cpu','ram'])
        data.save()
        messages.info(request,'Updated Successfully.')
        return redirect('cloud_manage_virtual_machine')
    return render(request,'cloud/cloud-edit-virtual-machine.html',{'i':i})


def cloud_manage_virtual_machine(request):
#    vm_id = request.session["vm_id"]
#    if request.method=='POST':
#         radio=request.POST['radio']
#         vm = vmModel.objects.create(radio=radio)
#         vm.save()

   data=vmModel.objects.all()

   return render(request,'cloud/cloud-manage-virtual-machine.html',{'data':data})



def cloud_on_status(request,id):
    on=get_object_or_404(vmModel,vm_id=id)
    on.status='ON'
    on.save(update_fields=['status'])
    on.save()
    return redirect('cloud_manage_virtual_machine')

def cloud_off_status(request,id):
    off=get_object_or_404(vmModel,vm_id=id)
    off.status='OFF'
    off.save(update_fields=['status'])
    off.save()
    return redirect('cloud_manage_virtual_machine') 



def cloud_task_scheduling_details(request):
   data =requestModel.objects.all().order_by("-request_id")
   if request.method=='POST':
         search=request.POST.get('search')
         data=requestModel.objects.filter(Q(request_id__icontains=search) | Q(vm_id__icontains=search) | Q(file_id__icontains=search) | Q(file_name__icontains=search))

   return render(request,'cloud/cloud-task-scheduling-details.html',{'data':data})




def cloud_load_balancer(request):

    file=vmModel.objects.all ()
    data1 = requestModel.objects.filter(vm_id=1).count()
    print(data1)
    data2 = requestModel.objects.filter(vm_id=2).count()
    print(data2)
    data3 = requestModel.objects.filter(vm_id=3).count()
 
   
    return render(request,'cloud/cloud-load-balancer.html',{'data1':data1,'data2':data2,'data3':data3,'file':file})



    
def cloud_makespan(request):
   app =requestModel.objects.all().order_by("-request_id")
   print(app)
   if request.method=='POST':
         search=request.POST.get('search')
         app=requestModel.objects.filter(Q(request_id__icontains=search) | Q(vm_id__icontains=search) | Q(file_name__icontains=search))


   return render(request,'cloud/cloud-makespan.html',{'app':app})
