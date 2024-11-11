"""algorithm_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ast import If
from xml.dom.minidom import Document


from django.conf.urls.static import static
from django.conf import settings
from cloudapp import views as cloudapp_views
from userapp import views as userapp_views
from mainapp import views as mainapp_views
from schedulerapp import views as schedulerapp_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',mainapp_views.home,name='home'),


# cloud

    path('cloud-login',cloudapp_views.cloud_login,name='cloud_login'),

    path('cloud-dashboard', cloudapp_views.cloud_dashboard,name='cloud_dashboard'),

    path('cloud-add-virtual-machine', cloudapp_views.cloud_add_virtual_machine,name='cloud_add_virtual_machine'),

    path('cloud-edit-virtual-machine/<int:id>/', cloudapp_views.cloud_edit_virtual_machine,name='cloud_edit_virtual_machine'),


    path('cloud-manage-virtual-machine', cloudapp_views.cloud_manage_virtual_machine,name='cloud_manage_virtual_machine'),

    path('cloud-task-scheduling-details', cloudapp_views.cloud_task_scheduling_details,name='cloud_task_scheduling_details'),

    path('cloud-on-status/<int:id>/',cloudapp_views.cloud_on_status,name='cloud_on_status'),

    path('cloud-off-status/<int:id>/',cloudapp_views.cloud_off_status,name='cloud_off_status'),

    path('cloud-load-balancer',cloudapp_views.cloud_load_balancer,name='cloud_load_balancer'),

    path('cloud-makespan',cloudapp_views.cloud_makespan,name='cloud_makespan'),


#task schedule


    path('scheduler-login',schedulerapp_views.scheduler_login,name='scheduler_login'),

    path('scheduler-dashboard', schedulerapp_views.scheduler_dashboard,name='scheduler_dashboard'),

    path('scheduler-assign-task', schedulerapp_views.scheduler_assign_task,name='scheduler_assign_task'),

    path('scheduler-task/<int:id>/', schedulerapp_views.scheduler_task,name='scheduler_task'),
   
    path('scheduler-manage-vm-resourses',schedulerapp_views.scheduler_manage_vm_resourses,name='scheduler_manage_vm_resourses'),

    path('scheduler-view-task',schedulerapp_views.scheduler_view_task,name='scheduler_view_task'),



#user

    path('user-otp',userapp_views.user_otp,name='user_otp'),

    path('user-login',userapp_views.user_login,name='user_login'),

    path('user-register', userapp_views.user_register,name='user_register'),

    path('user-dashboard', userapp_views.user_dashboard,name='user_dashboard'),

    path('user-upload-files',userapp_views.user_upload_files,name='user_upload_files'),

    path('user-view-files',userapp_views.user_view_files,name='user_view_files'),

    path('user-profile',userapp_views.user_profile,name='user_profile'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)