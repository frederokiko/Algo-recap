const express = require('express');
const router = express.Router();

// Route GET pour "Contact"
router.get('/', (req, res) => {
  res.send('Contactez-nous');
});

module.exports = router;
