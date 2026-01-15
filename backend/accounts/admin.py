from django.contrib import admin
from .models import LoginToken, SmsUser

admin.site.register(LoginToken)
admin.site.register(SmsUser)
