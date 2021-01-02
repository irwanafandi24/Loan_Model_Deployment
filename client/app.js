function getGenderValue(){
    var uiGender = document.getElementsByName("optionGender");
    for(var i in uiGender){
        if(uiGender[i].checked){
            return parseInt(i);
        }
    }
    return -1;
}

function getSelfEmployedValue(){
    var uiSelfEmployed = document.getElementsByName("optionEmployed");
    for(var i in uiSelfEmployed){
        if(uiSelfEmployed[i].checked){
            return parseInt(i);
        }
    }
    return -1;
}

function getMarriedValue(){
    var uiMarried = document.getElementsByName("optionMarried");
    for(var i in uiMarried){
        if(uiMarried[i].checked){
            return parseInt(i);
        }
    }
    return -1;
}

function onClickedPredictApproval(){
    console.log("Start to estimate the house price");
    var property_area = document.getElementById("uiPropertyArea");
    var gender = getGenderValue()
    var self_employed = getSelfEmployedValue()
    var married = getMarriedValue()
    var education = document.getElementById("uiEducation");
    var dependents = document.getElementById("uiDependents");
    var ap_income =document.getElementById("uiApIncome");
    var cap_income = document.getElementById("uiCapIncome");
    var loan_am = document.getElementById("uiLoanAm");
    var loan_amtrm = document.getElementById("uiLoanAmTrm");
    var credit_history = document.getElementById("uiCreditHistory");
    var approvalResult = document.getElementById("uiApprovalResult");

    console.log(gender, married, dependents.value, education.value, self_employed, ap_income.value, cap_income.value, loan_am.value, loan_amtrm.value, credit_history.value ,property_area.value)

//    var predict_url = "http://127.0.0.1:5000/predict_loan"
    var predict_url = "/predict_loan"
    $.post(predict_url, {
        gender : gender,
        married : married,
        dependents : parseInt(dependents.value),
        education : parseInt(education.value),
        self_employed : self_employed,
        applicant_income : parseInt(ap_income.value),
        coapplicant_income : parseInt(cap_income.value),
        loan_amount : parseInt(loan_am.value),
        loan_amount_term : parseInt(loan_amtrm.value),
        credit_history : parseInt(credit_history.value),
        property_area : property_area.value
    }, function(data, status){
        console.log("Approval result: ", data.classified_result);
        if (data.classified_result.toString() == 'Loan Approved'){
            approvalResult.innerHTML = "<h2 class='text-result-success'>"+data.classified_result.toString()+"</h2>"
        }else{
            approvalResult.innerHTML = "<h2 class='text-result-failed'>"+data.classified_result.toString()+"</h2>"
        }
    });
}

function onClickedReset(){
  var approvalResult = document.getElementById("uiApprovalResult");
  approvalResult.innerHTML = "<h2 class='text-result'>Approval Result</h2>";
}

function onPageLoad(){
    console.log("Load Location data from server");
//    var property_url = "http://127.0.0.1:5000/get_property_name";
    var property_url = "/get_property_name";
    $.get(property_url, function(data_property, status){
        console.log("Get Location response");
        if(data_property){
            var property = data_property.property_type;
            var uiarea = document.getElementById("uiPropertyArea");
            $('#uiPropertyArea').empty();
            for (var i in property){
                var opt = new Option(property[i]);
                $('#uiPropertyArea').append(opt);
                console.log(opt)
            }
        }
    });
}

window.onload = onPageLoad;
