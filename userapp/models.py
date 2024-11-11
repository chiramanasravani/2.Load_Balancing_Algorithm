
from django.db import models
from cloudapp.models import vmModel
from datetime import datetime
from datetime import time

# Create your models here.
# user register
class userModel(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_name=models.CharField(help_text='user_name',max_length=50)
    email=models.EmailField(help_text=' email', max_length=50)
    password=models.CharField(help_text='password', max_length=50)
    mobile=models.BigIntegerField(help_text='mobile')
    location=models.CharField(help_text='location', max_length=200)
    dob=models.DateField(help_text='dob')
    user_image=models.ImageField(upload_to='user_image', null=True)
    otp=models.IntegerField(null=True)
    verification=models.CharField(max_length=50,default='Pending')
    status=models.CharField(max_length=50,default='Pending',null="True")
    reg_date=models.DateField(auto_now_add=True)

    class Meta:
        db_table='user_details'


class fileModel(models.Model):
    file_id=models.AutoField(primary_key=True)
    # vm=models.ForeignKey(vmModel,db_column='vm_id', related_name='vm',on_delete=models.CASCADE,null=True,blank=True)
    user_id=models.IntegerField(null=True)
    vm_id=models.IntegerField(null=True)
    file=models.FileField(upload_to='files/' , null=True)
    file_name=models.CharField(help_text='file_name',max_length=200)
    description=models.CharField(help_text='description',max_length=250, null=True)
    file_extension=models.CharField(help_text='file_extension',max_length=250, null=True)
    file_size=models.BigIntegerField(help_text='file_size',null=True)
    file_type=models.CharField(help_text='file_type',max_length=300)
    file_key=models.CharField(null=True,max_length=200)
    file_data=models.TextField(null=True)
    status1=models.CharField(max_length=50,null="True")
    status=models.CharField(max_length=50,null="True",default='Pending')
    file_uploaded_date=models.DateField(auto_now_add=True, null=True)
    file_uploaded_time=models.CharField( null=True, max_length=250,)

    class Meta:
        db_table='file_details'         