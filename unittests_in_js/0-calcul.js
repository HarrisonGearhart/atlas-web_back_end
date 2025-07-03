#!/usr/bin/node
function calculateNumber(a, b) {
    const a_round = Math.round(a);
    const b_round = Math.round(b);

    return a_round + b_round;
}

module.exports = calculateNumber;
