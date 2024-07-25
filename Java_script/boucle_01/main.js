const htmltable=document.querySelector('table');

for (let i = 0; i < 8; i++) {
    
    const htmltr=document.createElement('tr');
    htmltable.appendChild(htmltr);
    
    
    
    for (let j = 0; j < 8; j++) {
        if(j%2!=0&&i%2!=0){
            
            const htmltd=document.createElement('td') ;
            //  htmltd=document.createAttribute('class');
             htmltd.classList.add('black');
            htmltr.appendChild(htmltd);
                }else if(j%2==0&&i%2==0){
                   
                    const htmltd=document.createElement('td') ;
                    //  htmltd=document.createAttribute('class');
                     htmltd.classList.add('black');
                    htmltr.appendChild(htmltd);
                   
                }else{
                    const htmltd=document.createElement('td') ;
                    //  htmltd=document.createAttribute('class');
                     htmltd.classList.add('blanc');
                    htmltr.appendChild(htmltd);
                }
        
                // const htmltd=document.createElement('td') ;
                // htmltr.appendChild(htmltd);
    }
}