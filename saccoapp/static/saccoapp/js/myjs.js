//setting the current date to the date field
window.onload = function(){ 
//getting the current date  
    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    var yyyy = today.getFullYear();
    today = dd + '/' + mm + '/' + yyyy;
    document.getElementById("date").value=today;

    //hide withdraw table
   // hideWithdrawTable()

}


//method to handle transaction type
function HandleTransactionType(){
    var transactionItems = document.getElementById("TransactionItems");
    var transactionType = transactionItems.options[transactionItems.selectedIndex].value;

        if(transactionType=="deposit"){
            document.getElementById("deposit_slip_div").style.display="block"
            document.getElementById("withdrawTable").style.display="none"

        }else if(transactionType=="withdraw"){
            document.getElementById("deposit_slip_div").style.display="none"
            document.getElementById("withdrawTable").style.display="table"
        }
}


//calculating total in the slip
function calculateTotal() {
    var transactionItems = document.getElementById("TransactionItems");
    var transactionType = transactionItems.options[transactionItems.selectedIndex].value;

if(transactionType=="deposit"){
var  fiftyNotevalue=document.getElementById("fiftyNote").value
var  twentyNotevalue=document.getElementById("twentyNote").value
var tenNotevalue=document.getElementById("tenNote").value
var  fivekNotevalue=document.getElementById("fivekNote").value
var twokNotevalue=document.getElementById("twokNote").value
var  onekNotevalue=document.getElementById("onekNote").value
var  onekCoinvalue=document.getElementById("onekCoin").value
var  fiveCoinvalue=document.getElementById("fiveCoin").value
var  twoCoinvalue=document.getElementById("twoCoin").value
var  oneCoinvalue=document.getElementById("oneCoin").value
var  fiftyCoinvalue=document.getElementById("fiftyCoin").value
var bankCharges=document.getElementById("bankcharges").value


var total=(Number(fiftyNotevalue)+Number(twentyNotevalue)+Number(tenNotevalue)+Number(fivekNotevalue)+Number(twokNotevalue)+Number(onekNotevalue)
+Number(onekCoinvalue)+Number(fiveCoinvalue)+Number(twoCoinvalue)+Number(oneCoinvalue)+Number(fiftyCoinvalue))

//alert(total)
//setting total value

document.getElementById("totalAmount").innerHTML=total+Number(bankCharges)

//setting amount to deposit
document.getElementById("amount").value=total


//setting bank charges
document.getElementById("charges").value=Number(bankCharges)


//setting slip number from data and transaction code
var today = new Date();
var dd = String(today.getDate()).padStart(2, '0');
var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
var yyyy = today.getFullYear();
var hour=today.getHours()
var minute=today.getMinutes()
var second=today.getSeconds()

today = dd +mm +yyyy+hour+minute+second;

var slipNumber="DP"+today
document.getElementById("slip_number").value=slipNumber


document.getElementById("submitButton").style.display="block"
document.getElementById("submitButton").disabled=false

}

}


function ShownetWithdraw(){
 var accountBalance= document.getElementById("accountBalance").innerHTML
 var minimumBalance= document.getElementById("minimumBalance").innerHTML

 var netWithdraw=(Number(accountBalance)-Number(minimumBalance))

 document.getElementById("netWithdraw").innerHTML=netWithdraw

 //setting slip number from data and transaction code
var today = new Date();
var dd = String(today.getDate()).padStart(2, '0');
var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
var yyyy = today.getFullYear();
var hour=today.getHours()
var minute=today.getMinutes()
var second=today.getSeconds()

today = dd +mm +yyyy+hour+minute+second;

var slipNumber="WD"+today
document.getElementById("slip_number").value=slipNumber

}


function ActivateDeactivateSubmitButton(){

//getting the transaction type
var transactionItems = document.getElementById("TransactionItems");
var transactionType = transactionItems.options[transactionItems.selectedIndex].value;


//check transaction type
if(transactionType=="withdraw"){

    var netWithdraw=document.getElementById("netWithdraw").innerHTML
    var amount= document.getElementById("amount").value

  if(Number(amount)>Number(netWithdraw)){
      document.getElementById("submitButton").style.display="none"
      document.getElementById("submitButton").disabled=true

  }else{
    document.getElementById("submitButton").style.display="block"
    document.getElementById("submitButton").disabled=false
  }

}

}

function hideWithdrawTable(){
    document.getElementById("withdrawTable").style.display="none"
}


