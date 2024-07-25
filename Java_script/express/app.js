//const express = require('express');
// const app = express();
// const port = 3000;

// app.get('/', (req, res) => {
//   res.send('Hello World!');
// });

// app.listen(port, () => {
//   console.log(`Example app listening at http://localhost:${port}`);
// });
//get
//post
//put
//patch
//delete
//etape 1
const express = require('express');
//etape 2
const app = express();
//etape 3
const port = 8000;

console.log("je commence ici");

//etape 5
app.get('/',(request,response)=>{
    response.writeHead(200);
    response.end("Ceci est un test !")
})




// lanement serveur etape 4
app.listen(port,() =>{
    console.log("serveur"+ port);
})