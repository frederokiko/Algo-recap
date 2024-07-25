// push ajoute à la fin 
// unshift ajoute au debut de la liste
// pop supprime
// shift() supprime le premier
// splice (1,2,'riri',fifi','loulou')
// tosplice() crée une copie
// .join(' - ') vouvou - tutu - nunu
// sort() 11,12,21,21,32,35,45,48
//sort (function(a,b){return a - b;});
// tosorted , avec copie
// reverse
// to reverse
// .slice(start,[end])  
// .include (264)
// find(function) + findlast(function)
// somme(fun ction) 
// filter( fonction )
//.map(function ) transforme
let li =Array()
let j=0
const htmltexte = document.querySelector('input');
const htmlbtn = document.querySelector('button');
const htmlp=document.querySelector('p');
const htmllu=document.querySelector('ol');

htmlbtn.addEventListener('click',function(){
    if(htmltexte.value.length>0){
    let texteret =htmltexte.value
    let result =Array();
    for (let i = 0; i < texteret.length; i++) {
        result.push(texteret[i]);
        
    }
    htmlp.textContent=result.reverse().join("");
    li.push(result.reverse().join(""));
    }else{
        htmlp.textContent="Veuillez entrer un texte valide"
    }
    htmlli=document.createElement('li');
    htmlli=document.textContent=li[j];
    htmllu.appendChild(htmlli);
    
   
    j++;
})