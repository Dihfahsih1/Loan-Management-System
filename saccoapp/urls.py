"""saccosystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url

from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^index$',index,name="index"),
    url(r'^register_member$',register_member, name="register_member"),
    url(r'^register_group$', register_group, name="register_group"),
    url(r'^group_members$', group_members, name="group_members"),
    url(r'^register_staff$', register_staff, name="register_staff"),
    url(r'^singleAccountTransaction$', singleAccountTransaction, name="singleAccountTransaction"),
    url(r'^groupAccountTransaction$', groupAccountTransaction, name="groupAccountTransaction"),
    url(r'^register_expense$',register_expense, name="register_expense"),
    url(r'^register_creditor_expense$', register_creditor_expense, name="register_creditor_expense"),
    url(r'^register_prepaid_expense$', register_prepaid_expense, name="register_prepaid_expense"),
    url(r'^register_income$', register_income, name="register_income"),
    url(r'^individual_loan$', individual_loan, name="individual_loan"),
    url(r'^group_loan$', group_loan, name="group_loan"),
    url(r'^loan_guarantor$', loan_guarantor, name="loan_guarantor"),
    url(r'^loan_consent$', loan_consent, name="loan_consent"),
    url(r'^view_members$', view_members, name="view_members"),
    url(r'^view_groups$', view_groups, name="view_groups"),
    url(r'^accountProfile$', accountProfile, name="accountProfile"),
    url(r'^changePassword$', changePassword, name="changePassword"),
    url(r'^view_member_details/(?P<pk>\d+)$', view_member_details, name="view_member_details"),
    url(r'^view_group_details/(?P<pk>\d+)$', view_group_details, name="view_group_details"),
    url(r'^view_group_members/(?P<pk>\d+)$', view_group_members, name="view_group_members"),
    url(r'^singleAccountTransacting/(?P<pk>\d+)$', singleAccountTransacting, name="singleAccountTransacting"),
    url(r'^groupAccountTransacting/(?P<pk>\d+)$', groupAccountTransacting, name="groupAccountTransacting"),
    url(r'^add_user_balance$', add_user_balance, name="add_user_balance"),
    url(r'^print_single_transaction/(?P<pk>\d+)$', print_single_transaction.as_view(), name="print_single_transaction"),
    url(r'^print_group_transaction/(?P<pk>\d+)$', print_group_transaction.as_view(), name="print_group_transaction"),
    url(r'^user_rights$', user_rights, name="user_rights"),

]
