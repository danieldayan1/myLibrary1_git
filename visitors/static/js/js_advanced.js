function loadCanvas(){

    let canvas = document.getElementById("myCanvas");
    let context = canvas.getContext("2d");

    //text
    context.font = "40px 'Segoe UI'";
    context.strokeText("welcom to my galery !!",150	,50)

    //house
    context.fillStyle = "blue";
    context.fillRect(300, 300, 100, 100);
    context.clearRect(335,375,30,25) 		//rect
    context.clearRect(320,320,20,25)
    context.clearRect(360,320,20,25)
    context.beginPath();				//roof
    context.moveTo(350, 250);
    context.lineTo(400, 300);
    context.lineTo(300, 300);
    context.fillStyle = "rgba(255, 0, 0, 0.75)"
    context.fill();							

    //smily sun
    context.beginPath();
    context.arc(75, 75, 50, 0, 2 * Math.PI, true); // Outer circle
    context.fillStyle = "yellow"
    context.fill();
    context.moveTo(110, 75);
    context.arc(75, 75, 35, 0, Math.PI, false);   // Mouth
    context.moveTo(65, 65);
    context.arc(60, 65, 5, 0, 2 * Math.PI, true);  // Left eye
    context.moveTo(95, 65);
    context.arc(90, 65, 5, 0, 2 * Math.PI, true);  // Right eye
    context.stroke();
        // draw individual dots for sun
    context.translate(75, 80);				
    for (let j = 0; j < 10; j++) {				
        context.rotate(2 * Math.PI / 10);
        context.beginPath();
        context.arc(0, 70, 10, 10, Math.PI * 2, true);
        context.fill();
        }


    //rings
    context.translate(0, 270);
    let ringsNum = 6;
        // Loop through rings (from inside to out)
    for (let i = 1; i < ringsNum; i++) {
        context.save();
        // set the fill color of the ring
        context.fillStyle = 'rgb(' + (50 * i) + ',' + (255 - 50 * i) + ',255)';
        // draw individual dots
        let numOfDots = 6 * i;
        for (let j = 0; j < numOfDots; j++) {
            context.rotate(2 * Math.PI / numOfDots);
            context.beginPath();
            context.arc(0, i * 12, 5, 0, Math.PI * 2, true);
            context.fill();
        }
        context.restore();
    }
}


////////////////////////////////////////////////////////////////////
function practice1(){
    let age = prompt("write your age: " , 20)
    if(age<18){
        alert("too young !!")
    }else if(age>18){
        alert("too old !!")
    }else{
        let cmd = confirm("you sure ?")
        if(cmd){
            alert ("happy 18 birthday !!!!!")
        }
    }
}
function practice2(){
     let names = ["david","sarah",23,"rivka",34]
     for(let i=0;i<names.length;i++){
        if (isNaN(names[i])){
            let name = names[i].toLocaleUpperCase()
            names.splice(i,1,name)
        }
     }
    alert(names);
    console.log(`names:  ${names}`);
}

