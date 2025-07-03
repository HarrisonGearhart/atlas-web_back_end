// 6-payment_token.test.js
const getPaymentTokenFromAPI = require('./6-payment_token');
const { expect } = require('chai');

describe('getPaymentTokenFromAPI', () => {
  it('should resolve with expected object when success is true', (done) => {
    getPaymentTokenFromAPI(true)
      .then((response) => {
        expect(response).to.deep.equal({ data: 'Successful response from the API' });
        done(); // signal Mocha test is complete and successful
      })
      .catch(done); // fail test if promise rejects
  });
});
