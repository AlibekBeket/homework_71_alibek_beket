from django.contrib import admin
from django.contrib.auth import get_user_model

from accounts.models import Account

# Register your models here.


admin.site.register(Account)
