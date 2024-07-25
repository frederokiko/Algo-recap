//let date =new Date(10000)
//let dte2 = getTime()
// mois de 0 à 11
// let birthdate = new Date(1973,3,30)
// console.log(birthdate);
// let date_jour = new Date()
// let result = date_jour.getFullYear()-birthdate.getFullYear();
// console.log(result);
let maintenant = new Date();
//let fin =new Date( new Date( new Date(today.setHours(17)).setMinutes(0) ).setSeconds(0));
let rfin = new Date();
let fin =rfin.setHours(17,0,0,0);
console.log(maintenant);
console.log(fin);
let result = fin -maintenant;
seconde=parseInt(result/1000)
console.log(seconde);
const htmlseconde=document.querySelector('h1')
htmlseconde.textContent=seconde +" secondes pour arriver à 17h00";
setInterval(function(){
    maintenant = new Date();
    result = fin -maintenant;
seconde=parseInt(result/1000);
    htmlseconde.textContent=seconde +" secondes pour arriver à 17h00";
},1000);
