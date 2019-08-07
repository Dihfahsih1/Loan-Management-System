from django import forms

from .models import *

class MemberForm(forms.ModelForm):
    class Meta:
        model=Member
        fields=('accountType','accountClassification','AccountNumber','SurName',
              'MiddleName','OtherName','Nationality','IDType','IDNumber','DateOfBirth','EmailAddress',
                'POBox','AreaOfResidence','District','RegisteredPhoneNumber','next_of_kin','relationship','NextOfKinPhysicalAddress','Photo',
                'Signature','DateOfJoining','MembershipFee','UserBalance')

class AccountSearchForm(forms.ModelForm):
    class Meta:
        model=AccountSearch
        fields=('accounts',)

class GroupAccountSearchForm(forms.ModelForm):
    class Meta:
        model=GroupAccountSearch
        fields=('group_accounts',)


class GroupForm(forms.ModelForm):
    class Meta:
        model=Group
        fields=('group_name','group_account_number','area_of_origin','district','group_id_number','account_balance','branch')

class StaffForm(forms.ModelForm):
    class Meta:
        model=Staff
        fields=('sur_name','middle_name','given_name','nationality',
              'ID_type','ID_number','date_Of_Birth','Email_Address','P_O_Box','Area_Of_Residence','District',
                'Registered_PhoneNumber','Next_Of_Kin_Physical_Address','next_of_kin','relationship','Photo','Signature','Date_Of_Joining',
                'Branch')

class ExpenseForm(forms.ModelForm):
    class Meta:
        model=Expense
        fields=('expense_item','amount_paid',
        'transaction_type','teller','branch')


class CreditorExpenseForm(forms.ModelForm):
    class Meta:
        model=CreditorExpense
        fields=('expense_date','expense_item','pending_balance','rate','quantity','transaction_details',
                'amount_paid','transaction_type','teller','branch')

class PrepaidExpenseForm(forms.ModelForm):
    class Meta:
        model=PrepaidExpense
        fields=('expense_date','expense_item','due_date','rate','quantity','amount_paid',
                'transaction_type','supplier','service_rendered','recurrency','reminders','transaction_details','teller','branch')

class IncomeForm(forms.ModelForm):
    class Meta:
        model=Income
        fields=('date','income_item','singleAccount','groupAccount','rate','quantity','payment_form',
                'amount_paid','transaction_details','receipt_number','teller','branch')


class IndividualLoanForm(forms.ModelForm):
    class Meta:
        model=IndividualLoan
        fields=('date','loan_status','individual_account','share_balance','loan_category','loan_category','loan_amount','form_fee','loan_purpose',
                'business_type','applicant_location','own_premises','legal_status_of_business','duration_in_business',
                'projected_investment_cost','own_contribution','monthly_net_profit','collateral_security_photo')


class GroupLoanForm(forms.ModelForm):
    class Meta:
        model=GroupLoan
        fields=('date','loan_status','group_account','loan_category','loan_category','loan_amount',
                'account_balance','withheld_deposit','form_fee')

class LoanGuarantorForm(forms.ModelForm):
    class Meta:
        model=LoanGuarantor
        fields=('date','guarantor_name','gender','loan_attached_to','phone','nationality',
                'ID_type','ID_number','physical_address')

class LoanConsentForm(forms.ModelForm):
    class Meta:
        model=LoanConsent
        fields=('date','consent_name','gender','loan_attached_to','phone','nationality',
                'ID_type','ID_number','physical_address')

class GroupMemberForm(forms.ModelForm):
    class Meta:
        model=GroupMember
        fields=('date','SurName','MiddleName','OtherName','nationality','attached_group','gender','profile_pic',
                'contact','address')

class UserBalanceForm(forms.ModelForm):
    class Meta:
        model=TellerAccountBalance
        fields=('user','amount','reason')


class AccountRightsForm(forms.ModelForm):
    class Meta:
        model=AccountRights
        fields=('user','can_deposit','can_withdraw','can_register','can_handle_loans',
        'can_send_balance')        