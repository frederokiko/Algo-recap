const express = require('express');
const router = express.Router();

// Route GET pour "À propos"
router.get('/', (req, res) => {
  res.send('À propos de nous');
});

module.exports = router;
