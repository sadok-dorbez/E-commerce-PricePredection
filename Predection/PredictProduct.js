const axios = require('axios');

function predict(req) {
  const inputData = {
    quantity: req.body.quantity,
    shipping: req.body.shipping,
    size: req.body.size,
    theme: req.body.theme,
  };

  return axios.post('http://127.0.0.1:6000/predict', inputData, {
    headers: { 'Content-Type': 'application/json' },
    responseType: 'json'
  });
}

module.exports = { predict };
