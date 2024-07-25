const couleur = document.getElementById('couleur');

couleur.addEventListener('input', (event) => {
    document.body.style.backgroundColor = event.target.value;
});
// const body=document.body;
// const inputcolor =document.querySelector('input[type=color]');
// const htmlbtn=document.querySelector('button');
// htmlbtn.addEventListener('click',function () {
//     body.innerHTML=
    
// })
let compteur = 1;

document.getElementById('afficherNombre').addEventListener('click',  () => {
    for (let index = 0; index <100; index++) {
        if (compteur <= 100) {
            document.getElementById('nombre').textContent = compteur;
            compteur++;
            
        } else {
            console.log("Tous les nombres de 1 à 100 ont été affichés !");
        } 
         pause(100);
    }
    
});