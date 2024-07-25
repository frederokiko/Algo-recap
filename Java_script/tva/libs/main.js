function tot(id){ 
    alert("fkgdskflgdlskf")
	let abal=document.getElementById("prix_u");
    let bbal=document.getElementById("quantite_u");
    a=parseInt(abal.value) ;
    b=parseInt(bbal.value);
        if(isNaN(a)||isNaN(b)){
            document.getElementById("idDeMaDiv").innerHTML ="Valeur incoherente";
            alert("Valeur incoherente")
        }else{
            let total = a*b;
            let totaltva= (total*21)/100
            document.getElementById("idDeMaDiv").innerHTML ="Le total est de : "+(total+ totaltva)+" €";
        }
 
}

let nombre_secret= Math.floor(Math.random() * 101);
let tour=0;

function verif(id){
   
	let anbr=document.getElementById("nbr_u"); 
    a=parseInt(anbr.value) ;
    
    console.log(a)
    tour+=1;
        if(a>nombre_secret){
            document.getElementById("result").innerHTML ="⬇ Le nombre secret est inférieur ==> Coups : "+tour;
            document.getElementById("new").innerHTML ="";
        }else if(a<nombre_secret){
          
            document.getElementById("result").innerHTML ="⬆ Le nombre secret est supérieur ==> Coups : "+tour;
            document.getElementById("new").innerHTML ="";
        }else{
            document.getElementById("result").innerHTML ="Bravo ✔ ,tu as trouvé c'étais bien le : "+nombre_secret +" en :"+tour+" coups";
            nombre_secret= Math.floor(Math.random() * 101);
            tour=0;
            document.getElementById("new").innerHTML ="Le nombre secret à été réinitialisé";
        }
 
}

const test = document.querySelector('.target')
console.log(test);
