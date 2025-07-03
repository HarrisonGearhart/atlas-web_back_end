const request = require('request');
const { expect } = require('chai');

describe('Index page', () => {
  const baseUrl = 'http://localhost:7865';

  it('should respond with status code 200', (done) => {
    request.get(baseUrl, (error, response, body) => {
      expect(error).to.be.null;
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should respond with the correct welcome message', (done) => {
    request.get(baseUrl, (error, response, body) => {
      expect(error).to.be.null;
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});

describe('Cart page', () => {
  const baseUrl = 'http://localhost:7865';

  it('should respond with 200 and correct message when id is a number', (done) => {
    request.get(`${baseUrl}/cart/12`, (error, response, body) => {
      expect(error).to.be.null;
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('should respond with 404 when id is NOT a number', (done) => {
    request.get(`${baseUrl}/cart/hello`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});
