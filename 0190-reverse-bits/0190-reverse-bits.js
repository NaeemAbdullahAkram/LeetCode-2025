/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function(n) {
    const reversed = BigInt(n).toString(2)
                              .split("")
                              .reverse()
                              .join("")
                              .padEnd(32, "0");
    return BigInt('0b' + reversed);
};