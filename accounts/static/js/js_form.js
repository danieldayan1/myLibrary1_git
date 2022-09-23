function showAge(val){
    doument.getElementById("show_Age").innerHtml = val
}

function timeToReset(){
    setInterval('resetPage()',480000);
}

function resetPage(){
    choose = confirm("you have been active for 2 minutes . Do you want to reset some of your fields?");
    if(choose){
        document.getElementById("myForm").reset();
    }
}

