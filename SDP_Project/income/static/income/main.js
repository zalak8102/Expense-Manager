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

function viewExp(id, csrftoken) {
    form = document.createElement('form');
    form.setAttribute('method','POST');
    form.setAttribute('action','/exp/viewExp/');
    input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'csrfmiddlewaretoken';
    input.value = csrftoken;
    form.appendChild(input);
    expse = document.createElement('input');
    expse.setAttribute('name','id');
    expse.setAttribute('type','hidden');
    expse.setAttribute('value',id);
    form.appendChild(expse);
    document.body.appendChild(form);
    form.submit();
}

function updExp(id, csrftoken) {
    form = document.createElement('form');
    form.setAttribute('method','POST');
    form.setAttribute('action','/exp/updateExp/');
    input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'csrfmiddlewaretoken';
    input.value = csrftoken;
    form.appendChild(input);
    expse = document.createElement('input');
    expse.setAttribute('name','id');
    expse.setAttribute('type','hidden');
    expse.setAttribute('value',id);
    form.appendChild(expse);
    document.body.appendChild(form);
    form.submit();
}

function delExp(id, csrftoken) {
    form = document.createElement('form');
    form.setAttribute('method','POST');
    form.setAttribute('action','/exp/del_exp/');
    input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'csrfmiddlewaretoken';
    input.value = csrftoken;
    form.appendChild(input);
    expse = document.createElement('input');
    expse.setAttribute('name','id');
    expse.setAttribute('type','hidden');
    expse.setAttribute('value',id);
    form.appendChild(expse);
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

function searchFun2() {
    var input = document.getElementById("gsearch");
    var filter = input.value.toLowerCase();
    var nodes = document.getElementsByClassName('d-flex mb-3 target');

    for (i = 0; i < nodes.length; i++) {
        var n = nodes[i].children[0];
        
        if (n.innerText.toLowerCase().includes(filter)) {
            for (j = 0; j < nodes[i].children.length; j++) {
                 nodes[i].children[j].style.display = "block";
            }
        } else {
            for (j = 0; j < nodes[i].children.length; j++) {
                nodes[i].children[j].style.display = "none";
            }
        }
    }
}
//$(".progress-bar").loading();