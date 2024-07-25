// const express = require('express');
// const router = express.Router();

// // Route GET pour l'accueil
// router.get('/', (req, res) => {
//   res.send('Accueil');
// });

// module.exports = router;

// Étape 1 : Importation d'express (des dépendances, modules, ...)
const express = require('express');
const router = require('./routes/home');


// Étape 2 : Initialisation du serveur express
const app = express();
app.use(router);

// Étape 3 : Définition du port du serveur
const PORT = 8000;



// Étape 4 : Écoute du port serveur
app.listen(PORT, () => {
    console.log(`Server is running on port : ${PORT}`)
});