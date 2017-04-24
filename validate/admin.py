from django.contrib import admin

from validate.models import Bank, Branch

from import_export.admin import ImportExportActionModelAdmin

class BankAdmin(ImportExportActionModelAdmin):
    pass

class BranchAdmin(ImportExportActionModelAdmin):
    pass

admin.site.register(Bank, BankAdmin)
admin.site.register(Branch, BranchAdmin)