// Router example
const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
  res.json({ message: 'Welcome to the AI-Powered Study Assistant API!' });
});

module.exports = router;