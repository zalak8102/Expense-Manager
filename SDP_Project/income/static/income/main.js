function updInc(id, csrftoken) {
    form = document.createElement('form');
    form.setAttribute('method','POST');
    form.setAttribute('action','/income/updateinc/');
    input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'csrfmiddlewaretoken';
    input.value = csrftoken;
    form.appendChild(input);
    income = document.createElement('input');
    income.setAttribute('name','id');
    income.setAttribute('type','hidden');
    income.setAttribute('value',id);
    form.appendChild(income);
    document.body.appendChild(form);
    form.submit();
}


function delInc(id, csrftoken) {
    form = document.createElement('form');
    form.setAttribute('method','POST');
    form.setAttribute('action','/income/del_income/');
    input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'csrfmiddlewaretoken';
    input.value = csrftoken;
    form.appendChild(input);
    income = document.createElement('input');
    income.setAttribute('name','id');
    income.setAttribute('type','hidden');
    income.setAttribute('value',id);
    form.appendChild(income);
    document.body.appendChild(form);
    form.submit();
}

function updPrf(email, csrftoken) {
    form = document.createElement('form');
    form.setAttribute('method','POST');
    form.setAttribute('action','/signup/updateprf/');
    input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'csrfmiddlewaretoken';
    input.value = csrftoken;
    form.appendChild(input);
    profile = document.createElement('input');
    profile.setAttribute('name','email');
    profile.setAttribute('type','hidden');
    profile.setAttribute('value',email);
    form.appendChild(profile);
    document.body.appendChild(form);
    form.submit();
}

function req(){
    if( document.getElementById('opwrd').required){
        document.getElementById('opwrd').required=false;
        document.getElementById('pwrd').required=false;
        document.getElementById('cpwrd').required=false;
    }
    else{
        document.getElementById('opwrd').required=true;
        document.getElementById('pwrd').required=true;
        document.getElementById('cpwrd').required=true;
    
    }
}

function passcheck(password,csrftoken){
    if(document.getElementById('opwrd').value!=password){
        document.getElementById('opwrd').value=null;
        window.alert("Enter correct password.");
    }
}

function oldpasscheck(password,csrftoken){
    if(document.getElementById('pwrd').value==password){
        document.getElementById('pwrd').value=null;
        window.alert("New password can not be same as a old password.");
    }
}

function newpasscheck(csrftoken){
    if(document.getElementById('pwrd').value!=document.getElementById('cpwrd').value){
        window.alert("Make sure your password and confirm password are same.");
    }
}

$(".progress-bar").loading();