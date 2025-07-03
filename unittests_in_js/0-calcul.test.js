#!/usr/bin/node
const assert = require('assert');
const calculateNumber = require("./0-calcul.js");

describe('calculateNumber', function () {
    it('should return 4 for (1, 3)', function () {
        assert.strictEqual(calculateNumber(1, 3), 4);
    });

    it('should return 5 for (1, 3.7)', function () {
        assert.strictEqual(calculateNumber(1, 3.7), 5);
    });

    it('should return 5 for (3.7, 1)', function () {
        assert.strictEqual(calculateNumber(3.7, 1), 5);
    });

    it('should return 6 for (2, 4.2)', function () {
        assert.strictEqual(calculateNumber(2, 4.2), 6);
    });

    it('should return 5 for (1.2, 3.7)', function () {
        assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    });

    it('should return 6 for (1.5, 3.7)', function () {
        assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    });

    it('should return 3 for (-1.5, 3.8)', function () {
        assert.strictEqual(calculateNumber(-1.5, 3.8), 3);
    });

    it('should return -2 for (-1.4, -1)', function () {
        assert.strictEqual(calculateNumber(-1.4, -1), 2);
    });
});