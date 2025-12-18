// Basic Express.js application setup
require('dotenv').config();
const express = require('express');
const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(express.json());

// Routes
app.use('/api', require('./routes'));

// Start server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});