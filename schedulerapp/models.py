from django.db import models

# Create your models here.


class requestModel(models.Model):
    request_id=models.AutoField(primary_key=True)
    # vm=models.ForeignKey(vmModel,db_column='vm_id', related_name='vm',on_delete=models.CASCADE,null=True,blank=True)
    user_id=models.IntegerField(null=True)
    vm_id=models.IntegerField(null=True)
    file_id=models.IntegerField(null=True)
    file=models.FileField(upload_to='files/' , null=True)
    file_name=models.CharField(help_text='file_name',max_length=200)
    description=models.CharField(help_text='description',max_length=250, null=True)
    file_size=models.BigIntegerField(help_text='file_size',null=True)
    file_type=models.CharField(help_text='file_type',max_length=300)

    file_data=models.TextField(null=True)
    # status=models.CharField(max_length=50,null="True",default='Pending')
    requested_date=models.DateField(auto_now_add=True, null=True)
    requested_time=models.CharField(max_length=300, null=True)
    file_uploaded_date=models.DateField(null=True)
    file_uploaded_time=models.CharField(max_length=300, null=True)
    differenced_time=models.CharField(null=True,max_length=300)
    

    

    class Meta:
        db_table='request_details' 