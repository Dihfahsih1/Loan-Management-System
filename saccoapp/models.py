# Create your models here.
from django.db import models
from django.db import models
from django.contrib.auth.models import User

from account.models import *


# Create your models here.

class Member(models.Model):

    accountTypes=(('FixedDeposit','FixedDeposit'),
        ('Savings', 'Savings'),
        ('Current', 'Current'),
        ('FixedPeriodSavings', 'FixedPeriodSavings'),
        ('Junior', 'Junior'))
    accountType = models.CharField(max_length=100, blank=False, choices=accountTypes)


    accountClassifications=(('Individual','Individual'),
        ('Joint', 'Joint'),
        ('IndividualGroupBased', 'IndividualGroupBased'),
        ('Group', 'Group'))

    accountClassification=models.CharField(max_length=100, blank=False, choices=accountClassifications)

    AccountNumber=models.CharField(max_length=100)

    SurName =models.CharField(max_length=100)

    MiddleName =models.CharField(max_length=100,blank=True,null=True)

    OtherName =models.CharField(max_length=100)

    FullName=models.CharField(max_length=100,default="")


    Nationality =models.CharField(max_length=100)

    IDtypes = (('NationalId', 'NationalId'),
                              ('Passport', 'Passport'),
                              ('DrivingPermit', 'DrivingPermit')
                              )

    IDType=models.CharField(max_length=100, blank=False, choices=IDtypes)

    IDNumber=models.CharField(max_length=100)

    DateOfBirth=models.CharField(max_length=100)

    EmailAddress=models.CharField(max_length=100)

    POBox=models.CharField(max_length=100)

    AreaOfResidence=models.CharField(max_length=100)

    District=models.CharField(max_length=100)

    RegisteredPhoneNumber=models.CharField(max_length=100)

    next_of_kin=models.CharField(max_length=100,null=True)

    NextOfKinPhysicalAddress=models.CharField(max_length=100)

    relationship=models.CharField(max_length=100,null=True)

    Photo=models.ImageField(max_length=100)

    Signature=models.ImageField(max_length=100)

    DateOfJoining=models.CharField(max_length=100)

    MembershipFee=models.CharField(max_length=100)

    UserBalance=models.FloatField(max_length=100,default=0.0,null=True)

    def save(self, *args, **kwargs):
        self.FullName=self.SurName+" "+self.MiddleName+" "+self.OtherName
        super(Member, self).save(*args, **kwargs)

    def __str__(self):
        return self.FullName+" | "+self.AccountNumber

class Group(models.Model):
    group_name=models.CharField(max_length=100)
    group_account_number=models.CharField(max_length=100)
    area_of_origin=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    group_id_number=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    account_balance=models.FloatField(max_length=100,default=0.0,null=True)
    def __str__(self):
        return self.group_name+" | "+self.district+" | "+self.group_account_number

class GroupMember(models.Model):
    date=models.CharField(max_length=100)
    SurName =models.CharField(max_length=100)
    MiddleName =models.CharField(max_length=100,blank=True,null=True)
    OtherName =models.CharField(max_length=100)
    FullName=models.CharField(max_length=100,default="")
    nationality=models.CharField(max_length=100)
    attached_group=models.ForeignKey(Group,on_delete=models.CASCADE, blank=True, null=True, default="")
    genderchoices = (('Male', 'Male'), ('Female', 'Female'))
    gender = models.CharField(max_length=50, blank=False, choices=genderchoices)
    profile_pic=models.ImageField(max_length=100)
    contact=models.CharField(max_length=100)
    address=models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.FullName=self.SurName+" "+self.MiddleName+" "+self.OtherName
        super(GroupMember, self).save(*args, **kwargs)

    def __str__(self):
        return self.FullName + "-" +str(self.attached_group)


class AccountSearch(models.Model):
    accounts=models.ForeignKey(Member,on_delete=models.CASCADE,null=True)

class GroupAccountSearch(models.Model):
    group_accounts=models.ForeignKey(Group,on_delete=models.CASCADE)

class Staff(models.Model):
    sur_name=models.CharField(max_length=100)
    middle_name=models.CharField(max_length=100,blank=True,null=True)
    given_name=models.CharField(max_length=100)
    full_Name = models.CharField(max_length=100, default="")
    nationality=models.CharField(max_length=100)
    IDtypes = (('NationalId', 'NationalId'),
                              ('Passport', 'Passport'),
                              ('DrivingPermit', 'DrivingPermit')
                              )
    ID_type=models.CharField(max_length=100, blank=False, choices=IDtypes)

    ID_number=models.CharField(max_length=100)
    date_Of_Birth=models.CharField(max_length=100)

    Email_Address=models.CharField(max_length=100)

    P_O_Box=models.CharField(max_length=100)

    Area_Of_Residence=models.CharField(max_length=100)

    District=models.CharField(max_length=100)

    Registered_PhoneNumber=models.CharField(max_length=100)

    next_of_kin=models.CharField(max_length=100)

    Next_Of_Kin_Physical_Address=models.CharField(max_length=100)

    relationship=models.CharField(max_length=100)

    Photo=models.ImageField(max_length=100)

    Signature=models.ImageField(max_length=100)

    Date_Of_Joining=models.CharField(max_length=100)

    Branch=models.CharField(max_length=100)

    def __str__(self):
        return self.full_Name + "-" + self.Branch

    def save(self, *args, **kwargs):
        self.full_Name=self.sur_name+" "+self.middle_name+" "+self.given_name
        super(Staff, self).save(*args, **kwargs)


class Transaction(models.Model):
    date=models.CharField(max_length=100)
    transaction_account=models.IntegerField(max_length=100,null=True)
    transaction_type=models.CharField(max_length=50)
    amount=models.FloatField(max_length=100,default=0.0)
    transacted_by=models.CharField(max_length=100)
    slip_number=models.CharField(max_length=100)
    transacting_staff=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    charges=models.CharField(max_length=100 ,default="",null=True)
    time_stamp=models.DateTimeField(auto_now_add=True)
    computer=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.amount+" | "+self.transaction_type

class GroupAccountTransaction(models.Model):
    date=models.CharField(max_length=100)
    transaction_account=models.IntegerField(max_length=100,null=True)
    transaction_type=models.CharField(max_length=50)
    amount=models.FloatField(max_length=100,default=0.0)
    transacted_by=models.CharField(max_length=100)
    slip_number=models.CharField(max_length=100)
    transacting_staff=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    charges=models.CharField(max_length=100 ,default="",null=True)
    time_stamp=models.DateTimeField(auto_now_add=True)
    computer=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.amount+" | "+self.transaction_type

   
            
class Expense(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    expense_item=models.CharField(max_length=100)
    amount_paid=models.FloatField(max_length=100,default=0.0)
    transactionchoices = (('Cash', 'Cash'),('Cheque', 'Cheque'))
    transaction_type=models.CharField(max_length=100, blank=False, choices=transactionchoices)
    teller=models.ForeignKey(Staff,on_delete=models.CASCADE)
    branch=models.CharField(max_length=100)

    def __str__(self):
        return self.expense_item+"-"+self.amount_paid

class CreditorExpense(models.Model):
    expense_date=models.CharField(max_length=100)
    expense_item=models.CharField(max_length=100)
    pending_balance=models.FloatField(max_length=100,default=0.0)
    rate=models.IntegerField(max_length=11)
    quantity=models.IntegerField(max_length=11)
    transaction_details=models.CharField(max_length=500)
    amount_paid=models.FloatField(max_length=100,default=0.0)
    transactionchoices = (('Cash', 'Cash'),('Cheque', 'Cheque'))
    transaction_type=models.CharField(max_length=100, blank=False, choices=transactionchoices)
    teller=models.ForeignKey(Staff,on_delete=models.CASCADE)
    branch=models.CharField(max_length=100)

    def __str__(self):
        return self.expense_item+"-"+self.amount_paid


class PrepaidExpense(models.Model):
    expense_date=models.CharField(max_length=100)
    expense_item=models.CharField(max_length=100)
    due_date=models.CharField(max_length=100)
    rate=models.IntegerField(max_length=11)
    quantity=models.IntegerField(max_length=11)
    amount_paid=models.FloatField(max_length=100,default=0.0)
    transactionchoices = (('Cash', 'Cash'),('Cheque', 'Cheque'))
    transaction_type=models.CharField(max_length=100, blank=False, choices=transactionchoices)
    supplier=models.CharField(max_length=100)
    service_rendered=models.CharField(max_length=100)
    recurrencychoices = (('Daily', 'Daily'),('Monthly', 'Monthly'),('Yearly', 'Yearly'))
    recurrency=models.CharField(max_length=100, blank=False, choices=recurrencychoices)
    reminders=models.CharField(max_length=100)
    transaction_details=models.CharField(max_length=500)
    teller=models.ForeignKey(Staff,on_delete=models.CASCADE)
    branch=models.CharField(max_length=100)

    def __str__(self):
        return self.expense_item+"-"+self.amount_paid

class Income(models.Model):
    date=models.CharField(max_length=100)
    income_item=models.CharField(max_length=100)
    singleAccount=models.ForeignKey(Member,on_delete=models.CASCADE,blank=True,null=True,default="")
    groupAccount=models.ForeignKey(Group,on_delete=models.CASCADE,blank=True,null=True,default="")
    rate = models.IntegerField(max_length=11)
    quantity = models.IntegerField(max_length=11)
    transactionchoices = (('Cash', 'Cash'), ('AccountDebit', 'AccountDebit'))
    payment_form = models.CharField(max_length=100, blank=False, choices=transactionchoices)
    amount_paid=models.FloatField(max_length=100,default=0.0)
    transaction_details=models.CharField(max_length=100)
    receipt_number=models.CharField(max_length=100)
    teller = models.ForeignKey(Staff, on_delete=models.CASCADE)
    branch = models.CharField(max_length=100)

    def __str__(self):
        return self.income_item + "-" + self.amount_paid


class IndividualLoan(models.Model):
    date=models.CharField(max_length=100)
    loanchoice=(('NewLoan','NewLoan'),('LoanTopUp','LoanTopUp'))
    loan_status=models.CharField(max_length=100, blank=False, choices=loanchoice)
    individual_account=models.ForeignKey(Member,on_delete=models.CASCADE,blank=True,null=True,default="")
    savings_balance=models.FloatField(max_length=100,default=0.0)
    share_balance=models.FloatField(max_length=100,default=0.0)
    loan_balance=models.FloatField(max_length=100,default=0.0)
    loan_category=models.CharField(max_length=100)
    loan_amount=models.FloatField(max_length=100,default=0.0)
    form_fee=models.FloatField(max_length=100,default=0.0)
    loan_purpose=models.CharField(max_length=100)
    business_type=models.CharField(max_length=100)
    applicant_location=models.CharField(max_length=100)

    prechoices=(('Yes','Yes'),('No','No'))
    own_premises=models.CharField(max_length=50, blank=False, choices=prechoices)
    legal_status_of_business=models.CharField(max_length=100)
    duration_in_business=models.CharField(max_length=100)
    projected_investment_cost=models.FloatField(max_length=100,default=0.0)
    own_contribution=models.FloatField(max_length=100,default=0.0)
    monthly_net_profit=models.FloatField(max_length=100,default=0.0)
    collateral_security_photo=models.ImageField(max_length=100)

    def __str__(self):
        return self.individual_account.FullName + "-" +str(self.loan_amount)

class GroupLoan(models.Model):
    date=models.CharField(max_length=100)
    loanchoice = (('NewLoan', 'NewLoan'), ('LoanTopUp', 'LoanTopUp'))
    loan_status = models.CharField(max_length=100, blank=False, choices=loanchoice)
    group_account = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True, default="")
    loan_category=models.CharField(max_length=100)
    loan_amount=models.FloatField(max_length=100,default=0.0)
    account_balance=models.FloatField(max_length=100,default=0.0)
    withheld_deposit=models.FloatField(max_length=100,default=0.0)
    form_fee=models.FloatField(max_length=100,default=0.0)

    def __str__(self):
        return self.group_account.group_name + "-" +str(self.loan_amount)


class LoanGuarantor(models.Model):
    date=models.CharField(max_length=100)
    guarantor_name=models.CharField(max_length=100)
    genderchoices = (('Male', 'Male'), ('Female', 'Female'))
    gender = models.CharField(max_length=50, blank=False, choices=genderchoices)
    loan_attached_to=models.ForeignKey(IndividualLoan,on_delete=models.CASCADE, blank=True, null=True, default="")
    phone=models.CharField(max_length=100)
    nationality=models.CharField(max_length=100)
    ID_types = (('NationalId', 'NationalId'),
               ('Passport', 'Passport'),
               ('DrivingPermit', 'DrivingPermit')
               )
    ID_type = models.CharField(max_length=100, blank=False, choices=ID_types)
    ID_number=models.CharField(max_length=100)
    physical_address=models.CharField(max_length=100)

    def __str__(self):
        return self.guarantor_name + "-" +str(self.loan_attached_to)


class LoanConsent(models.Model):
    date=models.CharField(max_length=100)
    consent_name=models.CharField(max_length=100)
    genderchoices = (('Male', 'Male'), ('Female', 'Female'))
    gender = models.CharField(max_length=50, blank=False, choices=genderchoices)
    loan_attached_to=models.ForeignKey(IndividualLoan,on_delete=models.CASCADE, blank=True, null=True, default="")
    phone=models.CharField(max_length=100)
    nationality=models.CharField(max_length=100)
    ID_types = (('NationalId', 'NationalId'),
               ('Passport', 'Passport'),
               ('DrivingPermit', 'DrivingPermit')
               )
    ID_type = models.CharField(max_length=100, blank=False, choices=ID_types)
    ID_number=models.CharField(max_length=100)
    physical_address=models.CharField(max_length=100)

    def __str__(self):
        return self.consent_name + "-" +str(self.loan_attached_to)




class companySettings(models.Model):
    company_name=models.CharField(max_length=100)
    company_logo=models.ImageField(max_length=100)
    branchName=models.CharField(max_length=100)
    minimum_account_balance=models.IntegerField(max_length=50)
    withdraw_charges=models.IntegerField(max_length=50,null=True)
    deposit_charges=models.IntegerField(max_length=50,null=True)

    def __str__(self):
       return self.company_name + "|" +self.branchName



class TellerAccountBalance(models.Model):
    date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(Account,on_delete=models.CASCADE, blank=True, null=True, default="")
    amount=models.IntegerField(max_length=50,default=0.0)  
    reason=models.CharField(max_length=200,null=True)
    time_stamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + "|" +str(self.amount)



class AccountRights(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE, blank=True, null=True, default="")
    can_deposit=models.BooleanField(default=False)
    can_withdraw=models.BooleanField(default=False)
    can_register=models.BooleanField(default=False)
    can_handle_loans=models.BooleanField(default=False)
    can_send_balance=models.BooleanField(default=False)

    def _str_(self):
        return str(self.user)

   













































































































