from django.contrib import admin
from .models import AuditCycle, AuditRecord

admin.site.register(AuditCycle)
admin.site.register(AuditRecord)