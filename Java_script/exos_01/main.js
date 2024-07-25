const data ={
    name:"ordinateur",
    factory : "dell",
    description : "super pc de merde",
    prix : 699.99,
    urlimage : "./pc.png"
};
const htmlProductName =document.querySelector('h1');
const htmlfactory =document.querySelector('h2');
const htmldescription = document.querySelector('p#desc')
const htmlprix = document.querySelector('p#price')
const htmlurl =document.querySelector('img')
htmlProductName.textContent =data.name;
htmlfactory.textContent=data.factory;
htmldescription.textContent=data.description;
htmlprix.textContent=data.prix
htmlurl.src=data.urlimage

//1 702 944 000 000