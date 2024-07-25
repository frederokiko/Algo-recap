const body = document.body;

// const htmlarticle=document.createElement('article');
// body.appendChild(htmlarticle);

// const htmlarttitre=document.createElement('h1');
// htmlarticle.appendChild(htmlarttitre);
// htmlarttitre.textContent="Coucou ca marche";

// const htmlartcontent =document.createElement('p');
// htmlarticle.appendChild(htmlartcontent);
// htmlartcontent.textContent="lorem ipsum";

// const htmlartinfo=document.createElement('p');
// htmlartinfo.textContent="on essaye ca aussi";
// htmlarticle.insertBefore(htmlartinfo,htmlarticle.children[1]);

// const htmlbefore = document.createElement('hr');
// const htmlhr = document.createElement('hr');
// htmlarticle.insertAdjacentElement('afterend',htmlhr);
// htmlarticle.insertAdjacentElement("beforebegin",htmlbefore);
const htmltache = document.querySelector('input');
const htmlbutton=document.querySelector('button');
const htmlol=document.querySelector('ol');
const htmlh1=document.querySelector('h1');
const htmlli=document.querySelector('li');
htmlbutton.addEventListener('click',function(){
    if(htmltache.value==""){
        alert("!!!Vous ne pouvez pas entrez de tache vide!!!")
    }else{
        htmlh1.remove();
        const htmlsup=document.createElement('button');
        
        const htmlli=document.createElement('li');
        htmlli.textContent=htmltache.value;
        htmlol.appendChild(htmlli);
        htmlli.addEventListener('click',function(){
            htmlli.remove();
            // htmlli.value.replace("");
        })
        htmltache.value = '';
    }
})

