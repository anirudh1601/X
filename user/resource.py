from import_export import resources 
from .models import AccountUser
class UserReportResource(resources.ModelResource):
     class Meta:
         model = AccountUser