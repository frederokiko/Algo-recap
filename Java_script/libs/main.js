// test
//? test
//! test
//todo test

// alert("Coucou , c'est nous !")
//?console.log("pas d'erreur");
//  a=parseInt(prompt("Entre un nombre")) ;
// b= parseInt(prompt("Entre un nombre")) ;
// let abal=document.getElementById("nbr1");
// let bbal=document.getElementById("nbr2");

//  a=abal.value;
//  b=bbal.value;
//?console.log(a+b);
function nom(id){
	let abal=document.getElementById("nbr1");
    let bbal=document.getElementById("nbr2");
    a=parseInt(abal.value) ;
    b=parseInt(bbal.value);
    document.getElementById("idDeMaDiv").innerHTML = a +" + "+ b+ " = " + (a+b);
}
function nom1(id){
	let abal=document.getElementById("nbr1");
    let bbal=document.getElementById("nbr2");
    a=parseInt(abal.value) ;
    b=parseInt(bbal.value);
    document.getElementById("idDeMaDiv").innerHTML = a +" - "+ b+ " = " + (a-b);
}
function nom2(id){
	let abal=document.getElementById("nbr1");
    let bbal=document.getElementById("nbr2");
    a=parseInt(abal.value) ;
    b=parseInt(bbal.value);
    document.getElementById("idDeMaDiv").innerHTML = a +" X "+ b+ " = " + (a*b);
}
function nom3(id){
	let abal=document.getElementById("nbr1");
    let bbal=document.getElementById("nbr2");
    a=parseInt(abal.value) ;
    b=parseInt(bbal.value);
        if(b!=0){
            document.getElementById("idDeMaDiv").innerHTML = a +" : "+ b+ " = " + (a/b);
        }else{
                document.getElementById("idDeMaDiv").innerHTML ="Division par 0 non acceptable";
                //!alert("Pas de division par 0")
            }
}














//! let baliseNom = document.getElementById("nom")
//! let nom = baliseNom.value
//! console.log(nom); 