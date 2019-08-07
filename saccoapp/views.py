# Create your views here.

from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from django.db.models import Count, F

from django.http import HttpResponse

from django.views.generic import View
from django.utils import timezone

from django.contrib.auth.forms import UserCreationForm

from django.views.decorators.http import require_http_methods

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import *
from django.core.paginator import Paginator
from account.views import *
from account.urls import *
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
import socket
from saccoapp.models import *
from datetime import date

from django.views.generic import View
from django.utils import timezone
from .pdf_render import Render


@login_required
def singleAccountTransaction(request):
    if request.method=="POST":
        form=AccountSearchForm(request.POST)
        if form.is_valid():
            account=form.cleaned_data['accounts']

            #getting the account transactions
            transactions=Transaction.objects.filter(transaction_account=account.pk).order_by('-id')[:3]

            form=AccountSearchForm()
            rights=get_object_or_404(AccountRights,user_id=request.user.id)
            context={'form':form,'account':account,'transactions':transactions,'rights':rights}
            return render(request,'singleAccountTransaction.html',context)
    else:
         #getting all the user rights
        rights=get_object_or_404(AccountRights,user_id=request.user.id)
        form=AccountSearchForm()
        context={'form':form,"rights":rights}
        return render(request,"singleAccountTransaction.html",context)
    rights=get_object_or_404(AccountRights,user_id=request.user.id)    
    form=AccountSearchForm()
    context={'form':form,'rights':rights}
    return render(request,"singleAccountTransaction.html",context)

@login_required
def groupAccountTransaction(request):
    if request.method=="POST":
        form=GroupAccountSearchForm(request.POST)
        if form.is_valid():
            account=form.cleaned_data['group_accounts']

            #getting the account transactions
            transactions=GroupAccountTransaction.objects.filter(transaction_account=account.pk).order_by('-id')[:3]

            form=GroupAccountSearchForm()
            context={'form':form,'account':account,'transactions':transactions}
            return render(request,'groupAccountTransaction.html',context)
    else:
        form=GroupAccountSearchForm()
        context={'form':form}
        return render(request,"groupAccountTransaction.html",context)
    form=GroupAccountSearchForm()
    context={'form':form}
    return render(request,"groupAccountTransaction.html",context)


@login_required
def singleAccountTransacting(request,pk):
    #getting the computer name
    computerName = socket.gethostname()

    #getting the transaction object
    transaction_obj=Transaction()

    #get account Balance
    accountBal=get_object_or_404(Member,pk=pk).UserBalance

    #get the minimum balance on account
    companySetting=get_object_or_404(companySettings,id=1)


    if request.method=="POST":
        date = request.POST['date']
        transaction_type=request.POST['transaction']
        amount=request.POST['amount']     
        transacted_by=request.POST['transacted_by']
        slip_number=request.POST['slip_number']
        transacting_staff=request.POST['transacting_staff']
        branch=request.POST['branch']
        charges=request.POST['charges']
        computer=request.POST['computer']

        transaction_obj.date=date
        transaction_obj.transaction_account=pk
        transaction_obj.transaction_type=transaction_type
        transaction_obj.amount=amount
        transaction_obj.transacted_by=transacted_by
        transaction_obj.slip_number=slip_number
        transaction_obj.transacting_staff=transacting_staff
        transaction_obj.branch=branch
        transaction_obj.charges=charges
        transaction_obj.computer=computer

        #get account Balance
        accountBal=get_object_or_404(Member,pk=pk).UserBalance

        #update account balance on deposit
        if transaction_type=="deposit":
            #the total
            total=float(amount)+float(charges)

            Member.objects.filter(pk=pk).update(UserBalance=F('UserBalance')+amount)

            #updating account user balance
            Account.objects.filter(pk=request.user.pk).update(User_balance=F('User_balance')+total)

            messsage="Successfully deposited "+amount+" UGX" 

        #update account after withdrawal of money
        elif transaction_type=="withdraw":
            #the total
            total=float(amount)+float(charges)

            Member.objects.filter(pk=pk).update(UserBalance=F('UserBalance')-total)

            #updating account user balance
            Account.objects.filter(pk=request.user.pk).update(User_balance=F('User_balance')-amount)
    
            messsage="Successfully withdrawn "+amount+" UGX"   

        #saving the transaction
        transaction_obj.save()   

        #getting the account details
        account=get_object_or_404(Member,pk=pk)

        #setting content to context
        context={'message':messsage,"transaction":transaction_obj,"account":account}

        # redirection to success page and print receipt
        return render(request,"single_transaction_success.html",context)

    else:
        return render(request,"singleAccountTransacting.html",{"computerName":computerName,"companySetting":companySetting,"accountBal":accountBal})

    return render(request,"singleAccountTransacting.html",{"computerName":computerName,"companySetting":companySetting,"accountBal":accountBal})



@login_required
def groupAccountTransacting(request,pk):
    #getting the computer name
    computerName = socket.gethostname()

    #getting the transaction object
    transaction_obj=GroupAccountTransaction()

    #get account Balance
    accountBal=get_object_or_404(Group,pk=pk).account_balance

    #get the minimum balance on account
    companySetting=get_object_or_404(companySettings,id=1)


    if request.method=="POST":
        date = request.POST['date']
        transaction_type=request.POST['transaction']
        amount=request.POST['amount']     
        transacted_by=request.POST['transacted_by']
        slip_number=request.POST['slip_number']
        transacting_staff=request.POST['transacting_staff']
        branch=request.POST['branch']
        charges=request.POST['charges']
        computer=request.POST['computer']

        transaction_obj.date=date
        transaction_obj.transaction_account=pk
        transaction_obj.transaction_type=transaction_type
        transaction_obj.amount=amount
        transaction_obj.transacted_by=transacted_by
        transaction_obj.slip_number=slip_number
        transaction_obj.transacting_staff=transacting_staff
        transaction_obj.branch=branch
        transaction_obj.charges=charges
        transaction_obj.computer=computer

        #get account Balance
        accountBal=get_object_or_404(Group,pk=pk).account_balance

        #update account balance on deposit
        if transaction_type=="deposit":
            Group.objects.filter(pk=pk)\
            .update(account_balance=F('account_balance')+amount)

            #the total
            total=float(amount)+float(charges)

            #updating account user balance
            Account.objects.filter(pk=request.user.pk).update(User_balance=F('User_balance')+total)

            messsage="Successfully deposited"+ amount+" UGX" 

        #update account after withdrawal of money
        elif transaction_type=="withdraw":

            #the total
            total=float(amount)+float(charges)

            #update the group account balance
            Group.objects.filter(pk=pk)\
                .update(account_balance=F('account_balance')-total)

            #updating account user balance
            Account.objects.filter(pk=request.user.pk).update(User_balance=F('User_balance')-amount)
    
            messsage="Successfully withdrawn "+amount+" UGX"   

        #saving the transaction
        transaction_obj.save()   

        #getting the account details
        account=get_object_or_404(Group,pk=pk)  

        #setting content to context
        context={'message':messsage,"transaction":transaction_obj,"account":account}

        # redirection to success page and print receipt
        return render(request,"group_transaction_success.html",context)
    else:
        return render(request,"groupAccountTransacting.html",{"computerName":computerName,"companySetting":companySetting,"accountBal":accountBal})

    return render(request,"groupAccountTransacting.html",{"computerName":computerName,"companySetting":companySetting,"accountBal":accountBal})

class print_single_transaction(View):
    def get(self, request,pk):
        #driver id to match drivers in payment table
        account = get_object_or_404(Member, pk=pk)
        #passing on the driver attached car
        transaction=Transaction.objects.filter(transaction_account=pk).latest('id')

        #getting today's date
        today = timezone.now()

        #parameters sent to the pdf for display
        params = {
            'account':account,
            'transaction':transaction,
            'today': today,
        }
        return Render.render('print_single_transaction.html', params)


class print_group_transaction(View):
    def get(self, request,pk):
        #driver id to match drivers in payment table
        account = get_object_or_404(Group, pk=pk)
        #passing on the driver attached car
        transaction=GroupAccountTransaction.objects.filter(transaction_account=pk).latest('id')

        #getting today's date
        today = timezone.now()

        #parameters sent to the pdf for display
        params = {
            'account':account,
            'transaction':transaction,
            'today': today,
        }
        return Render.render('print_group_transaction.html', params)

@login_required
def index(request):
    #getting all the user rights
    rights=get_object_or_404(AccountRights,user_id=request.user.id)
    context={"rights":rights}
    return render(request,"index.html",context)

@login_required
def register_member(request):
    if request.method=="POST":
        form=MemberForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_members')
    else:
        form=MemberForm()
        items = Member.objects.all()
        context = {'items': items,'form': form }
        return render(request, "register_member.html",context)

@login_required
def view_members(request):
    #search request with account number
    if request.method == 'POST':
        accountNo = request.POST['accountNo']
        account=get_object_or_404(Member,AccountNumber=accountNo)
        if account is None:
            message="account is not available"
            return render(request,'view_members.html',{'message':message})
        else:
            return render(request,'view_member_details.html',{'account':account})
    else:
        members = Member.objects.all()
        paginator = Paginator(members, 4)
        page = request.GET.get('page')
        items = paginator.get_page(page)
        context = {'items': items}
        return render(request, "view_members.html", context)

@login_required
def view_groups(request):
    #search request with account number
    if request.method == 'POST':
        accountNo = request.POST['accountNo']
        account=get_object_or_404(Member,AccountNumber=accountNo)
        if account is None:
            message="account is not available"
            return render(request,'view_groups.html',{'message':message})
        else:
            return render(request,'view_member_details.html',{'account':account})
    else:
        groups = Group.objects.all()
        paginator = Paginator(groups, 4)
        page = request.GET.get('page')
        items = paginator.get_page(page)
        context = {'items': items}
        return render(request, "view_groups.html", context)

@login_required
def view_member_details(request,pk):
    account=get_object_or_404(Member,pk=pk)
    return render(request,'view_member_details.html',{'account':account})

@login_required
def view_group_details(request,pk):
    account=get_object_or_404(Group,pk=pk)
    return render(request,'view_group_details.html',{'account':account})


@login_required
def register_group(request):
    if request.method=="POST":
        form=GroupForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_groups')
    else:
        form=GroupForm()
        items = Group.objects.all()
        context = {'items': items,'form': form }
        return render(request, "register_group.html",context)

@login_required
def group_members(request):
    if request.method=="POST":
        form=GroupMemberForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_groups')
    else:
        form=GroupMemberForm()
        items = GroupMember.objects.all()
        context = {'items': items,'form': form }
        return render(request, "group_members.html",context)

@login_required
def register_staff(request):
    if request.method=="POST":
        form=StaffForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('register_staff')
    else:
        form=StaffForm()
        items = Staff.objects.all()
        context = {'items': items,'form': form }
        return render(request, "register_staff.html",context)

@login_required
def register_expense(request):
    if request.method=="POST":
        form=ExpenseForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('register_expense')
    else:
        form=ExpenseForm()
        items = Expense.objects.all()
        context = {'items':items,'form':form }
        return render(request, "register_expense.html",context)   

@login_required
def register_income(request):
    if request.method=="POST":
        form=IncomeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('register_income')
    else:
        form=IncomeForm()
        items = Income.objects.all()
        context = {'items':items,'form':form }
        return render(request, "register_income.html",context)

@login_required
def individual_loan(request):
    if request.method=="POST":
        form=IndividualLoanForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('individual_loan')
    else:
        form=IndividualLoanForm()
        items = IndividualLoan.objects.all()
        context = {'items':items,'form':form }
        return render(request, "individual_loan.html",context)

@login_required
def group_loan(request):
    if request.method=="POST":
        form=GroupLoanForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('group_loan')
    else:
        form=GroupLoanForm()
        items = GroupLoan.objects.all()
        context = {'items':items,'form':form }
        return render(request, "group_loan.html",context)

@login_required
def loan_guarantor(request):
    if request.method=="POST":
        form=LoanGuarantorForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('loan_guarantor')
    else:
        form=LoanGuarantorForm()
        items = LoanGuarantor.objects.all()
        context = {'items':items,'form':form }
        return render(request, "loan_guarantor.html",context)

@login_required
def loan_consent(request):
    if request.method=="POST":
        form=LoanConsentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('loan_consent')
    else:
        form=LoanConsentForm()
        items = LoanConsent.objects.all()
        context = {'items':items,'form':form }
        return render(request, "loan_consent.html",context)

@login_required
def register_creditor_expense(request):
    if request.method=="POST":
        form=CreditorExpenseForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('register_creditor_expense')
    else:
        form=CreditorExpenseForm()
        items = CreditorExpense.objects.all()
        context = {'items':items,'form':form }
        return render(request, "register_creditor_expense.html",context)

@login_required
def register_prepaid_expense(request):
    if request.method=="POST":
        form=PrepaidExpenseForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('register_prepaid_expense')
    else:
        form=PrepaidExpenseForm()
        items = PrepaidExpense.objects.all()
        context = {'items':items,'form':form }
        return render(request, "register_prepaid_expense.html",context)



@login_required
def accountProfile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    context={} 
    if request.POST:
        form=AccountUpdateForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=AccountUpdateForm(
            initial={
                "email":request.user.email,
                "username":request.user.username, 
                "photo":request.user.Photo,
            }
        )  
    context['account_form']=form
    return render(request,'accountProfile.html',context)    




@login_required
def changePassword(request):
    if not request.user.is_authenticated:
        return redirect('login')
    context={} 
    if request.POST:
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('index')
    else:
        form=PasswordChangeForm(user=request.user)  
    context['account_form']=form
    return render(request,'changePassword.html',context)  

@login_required
def view_group_members(request,pk):
    if request.method=="POST":
        form=AccountSearchForm(request.POST)
        if form.is_valid():
            account=form.cleaned_data['accounts']

            #getting the current date first
            today = date.today()
            datetoday = today.strftime("%d/%m/%Y")

            #getting the group instance
            grp=get_object_or_404(Group,pk=pk)

            #getting account details
            SurName=account.SurName
            MiddleName=account.MiddleName
            OtherName=account.OtherName
            FullName=account.FullName
            nationality=account.Nationality
            attached_group=grp
            gender="unknown"
            profile_pic=account.Photo
            contact=account.RegisteredPhoneNumber
            address="unknown"

            #create a group member object
            groupMember=GroupMember()

            #attach account details to the object
            groupMember.date=datetoday
            groupMember.SurName=SurName
            groupMember.MiddleName=MiddleName
            groupMember.OtherName=OtherName
            groupMember.FullName=FullName
            groupMember.nationality=nationality
            groupMember.attached_group=attached_group
            groupMember.gender=gender
            groupMember.profile_pic=profile_pic
            groupMember.contact=contact
            groupMember.address=address

            #save the group member object
            groupMember.save()

            return redirect('view_groups')

        else:
            members=GroupMember.objects.filter(attached_group=pk)
            form=AccountSearchForm()
            context={'members':members,'form':form}
            return render(request,'view_group_members.html',context) 

    members=GroupMember.objects.filter(attached_group=pk)
    form=AccountSearchForm()
    context={'members':members,'form':form}
    return render(request,'view_group_members.html',context)    

@login_required
def add_user_balance(request):
    if request.method=="POST":
        form=UserBalanceForm(request.POST,request.FILES)
        if form.is_valid():
            #update the user baalance
            user=form.cleaned_data['user']
            amount=form.cleaned_data['amount']

            #update the user balance
            Account.objects.filter(pk=user.pk).update(User_balance=F('User_balance')+amount)

            #save the form
            form.save()

            #message
            #message="successfully added "+str(amount)+" to "+user.username
            return redirect('add_user_balance')
    else:
        form=UserBalanceForm()
        return render(request,'add_user_balance.html',{'form':form})

    form=UserBalanceForm()
    return render(request,'add_user_balance.html',{'form':form})

@login_required
def user_rights(request):
    if request.method=="POST":
        form=AccountRightsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user_rights')
    else:
        all_user_rights=AccountRights.objects.all()
        form=AccountRightsForm()
        context = {'form':form,'userrights':all_user_rights}
        return render(request, "user_rights.html",context)



