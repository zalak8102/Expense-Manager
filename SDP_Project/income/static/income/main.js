
/*function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

window.onclick = function (event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}

function createFolder(csrftoken) {
    var foldername = prompt("Please enter foldername:");
    form = document.createElement('form');
    form.setAttribute('method','POST');
    form.setAttribute('action','/user/createfolder/');
    input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'csrfmiddlewaretoken';
    input.value = csrftoken;
    form.appendChild(input);
    file = document.createElement('input');
    file.setAttribute('name','newfolder');
    file.setAttribute('type','hidden');
    file.setAttribute('value',foldername);
    form.appendChild(file);
    document.body.appendChild(form);
    form.submit();l̥
}

function download(filename, csrftoken) {
    form = document.createElement('form');
    form.setAttribute('method','POST');
    form.setAttribute('action','/user/download/');
    input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'csrfmiddlewaretoken';
    input.value = csrftoken;
    form.appendChild(input);
    file = document.createElement('input');
    file.setAttribute('name','filename');
    file.setAttribute('type','hidden');
    file.setAttribute('value',filename);
    form.appendChild(file);
    document.body.appendChild(form);
    form.submit();
}
*/
function upd(id, csrftoken) {
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


function del(id, csrftoken) {
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
