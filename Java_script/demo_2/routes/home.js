const express = require('express');
const router = express.Router();

// Route GET pour l'accueil
router.get('/', (req, res) => {
  res.send('Accueil');
});
router.get('/fred', (req, res) => {
  res.writeHead(200, {
    
      'Content-Type': 'text/html'
  });
  res.end('<h1>Bonjour fred</h1>');
});
router.get('/nom', (req, res) => {
  res.writeHead(200, {
      'Content-Type': 'text/html'
  });
  res.end('<h1>nom</h1>');
});
// ceci est bon pour recuperer un id via l'url

router.get('/id/:text', (req, res) => {
  const param = req.params.text;
  res.writeHead(200, {
      'Content-Type': 'text/html'
  });
  res.end(`<h1>l'id est : ${param}</h1>`);
});
module.exports = router;
