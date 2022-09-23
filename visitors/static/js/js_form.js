function showAge(val){
    doument.getElementById("show_Age").innerHtml = val
}

function checkStorageSupport() {
    if (!window.localStorage) {
        alert('This browser does NOT support localStorage');
}
}

function savePasswordName() {
    let userName = document.getElementById("name").value;
    let pass = document.getElementById("password").value;
    localStorage.userName = userName;
    localStorage.password = pass;
    alert("Username and password saved successfully");
}	           
function getPasswordName(){
    document.getElementById("name").value = localStorage.userName;
    document.getElementById("password").value = localStorage.password;
    alert("Welcome again: " + localStorage.userName);
}

function checkCookie(){
    let user = getCookie("userName");
    let pass = getCookie("password");

    if (user != "" && pass != " "){
      document.getElementById("name").value = user;
      document.getElementById("password").value = pass;
      alert("Welcome again: " + user);
    } 
}
function setCookie(){
    name_val = document.getElementById("name").value; ;
    pass_val = document.getElementById("password").value;
    document.cookie = "userName=" + name_val + ";" + "password=" + pass_val + ";" + ";path=/";
}  
function getCookie(cname){
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i < ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
}  



function chackPassword(){
    let pass = document.getElementById("password");
    let confirmPass = document.getElementById("confirmPassword");
    
    if(pass.value != confirmPass.value)
        confirmPass.setCustomValidity("Passwords do not match");
    else
         confirmPass.setCustomValidity("");
}

function chackEmail(){
    let mail = document.getElementById("mail").value
    if(mail.indexOf("@")== -1)
        alert("wrong mail !")
}

function timeToReset(){
    setInterval('resetPage()',240000);
}

function resetPage(){
    choose = confirm("you have been active for 60 seconds . Do you want to reset some of your fields?");
    if(choose){
        document.getElementById("myForm").reset();
    }
}

function sumbitForm(){
    let myUrl = "http://localhost:8080/?"
    let name =  document.getElementById("name").value;
    let pass =  document.getElementById("password").value;

    let newUrl = myUrl+"name:"+name+"&"+"password:"+pass;
    document.getElementById("myForm").setAttribute("action",newUrl)
}
