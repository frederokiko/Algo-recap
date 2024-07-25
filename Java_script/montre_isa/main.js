const htmlnbr=document.querySelector('input');
const htmlbtn = document.querySelector('button');
const htmlp=document.querySelector('h4');

htmlbtn.addEventListener('click',function(){
    let resultat =htmlnbr.value * 2;
    console.log(resultat);
    htmlp.textContent=resultat;
})