const htmltable= document.querySelector('table');
const tab =function(lignes,colonnes){
    for (let i = 0; i < lignes+1; i++) {
        const htmltr=document.createElement('tr');
        htmltable.appendChild(htmltr);
        for (let j = 0; j < colonnes; j++) {
                const htmltd=document.createElement('td') ;
                htmltr.appendChild(htmltd);
                if(i == lignes){
                    const htmlbtn=document.createElement('button');
                    htmlbtn.textContent = '+';
                    htmltd.appendChild(htmlbtn) ;

                }
        
        }
    }

};

//GO
tab(6,7);
const htmlbtn1=document.querySelector('button');

htmlbtn1.addEventListener('click',function(){
    console.log("ceci est un test1");
});

