const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', () => {
  describe('SUM', () => {
    it('should return the sum of rounded numbers', () => {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
      expect(calculateNumber('SUM', 2.6, 3.3)).to.equal(6);
      expect(calculateNumber('SUM', -1.2, -2.8)).to.equal(-4);
    });
  });

  describe('SUBTRACT', () => {
    it('should return the difference of rounded numbers', () => {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
      expect(calculateNumber('SUBTRACT', 5.5, 2.2)).to.equal(4);
      expect(calculateNumber('SUBTRACT', -1.5, -2.5)).to.equal(1);
    });
  });

  describe('DIVIDE', () => {
    it('should return the division of rounded numbers', () => {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
      expect(calculateNumber('DIVIDE', 4.6, 2.1)).to.equal(2.5);
    });

    it('should return "Error" when dividing by 0', () => {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
      expect(calculateNumber('DIVIDE', 1.4, 0.2)).to.equal('Error');
    });
  });

  describe('Invalid type', () => {
    it('should throw an error for an unsupported operation', () => {
      expect(() => calculateNumber('MULTIPLY', 1, 2)).to.throw('Invalid operation type');
    });
  });
});
