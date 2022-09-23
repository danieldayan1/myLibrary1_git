window.status = "Welcome to my site!";

var myInterval;
var currentImage = 0
var animationStarted = false;
var arr = new Array();
function PreloadImages(){
var pic = new Image();
    arr[0] = "PIC4.jfif";
    arr[1] = "PIC3.jfif";
    arr[2] = "PIC2.jfif";
    arr[3] = "PIC1.jfif";
    for (var i=0; i < 4; i++){
        pic.src = "{%static " + "'" + arr[i] + "'%}";
    }
    StartAnimation();
}
function ChangeImage(){
    let img =   "url(" + arr[currentImage] + ")"
    document.getElementById("header").style.backgroundImage =  img; 
    document.getElementById("header").style.backgroundRepeat = "no-repeat" ; 
    document.getElementById("header").style.backgroundSize = " 100% 100%" ;

    if (currentImage >= 3){
        currentImage = 0;
    }else{
        currentImage =  currentImage + 1;
    }
}
function StartAnimation(){
    if (animationStarted == false){
        myInterval = setInterval("ChangeImage()", 2000)
        animationStarted = true;
    }
}

