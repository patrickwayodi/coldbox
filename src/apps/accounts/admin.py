from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AccountCreationForm, AccountChangeForm
from .models import Account


class AdminAccount(UserAdmin):

    add_form = AccountCreationForm

    form = AccountChangeForm

    model = Account

    list_display = ['email', 'username',]


admin.site.register(Account, AdminAccount)
