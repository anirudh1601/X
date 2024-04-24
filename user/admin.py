from import_export.admin import ImportExportModelAdmin
from django.contrib import admin 
from .resource import UserReportResource  
from .models import AccountUser
class ReportAdmin(ImportExportModelAdmin):
     resource_class = UserReportResource   

admin.site.register(AccountUser, ReportAdmin)
