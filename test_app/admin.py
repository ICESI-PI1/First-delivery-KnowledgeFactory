from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Company)
admin.site.register(Project)
admin.site.register(Role)
admin.site.register(Roles)
admin.site.register(Binnacle)
admin.site.register(Meeting)
admin.site.register(Quotation)