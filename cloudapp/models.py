from django.db import models

# Create your models here.


class vmModel(models.Model):
    vm_id=models.AutoField(primary_key=True)
    vm_name=models.CharField(help_text='vm_name',max_length=50)
    os=models.CharField(help_text=' os', max_length=50)
    storage=models.CharField(help_text='storage', max_length=50)
    storage_type=models.CharField(help_text='storage_type', max_length=50,null=True)
    cpu=models.CharField(help_text='cpu', max_length=50)
    ram=models.CharField(help_text='ram', max_length=200)
    vm_added_date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=50,default='Pending',null="True")
    radio=models.CharField(max_length=50,default='Pending',null="True")
    class Meta:
        db_table='vm_details'
