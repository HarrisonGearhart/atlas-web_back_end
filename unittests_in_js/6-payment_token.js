// 6-payment_token.js
function getPaymentTokenFromAPI(success) {
    if (success) {
      return Promise.resolve({ data: 'Successful response from the API' });
    }
    // If success is false, function does nothing (implicitly returns undefined)
  }
  
  module.exports = getPaymentTokenFromAPI;
  