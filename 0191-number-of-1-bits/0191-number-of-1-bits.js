/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function(n) {
let a= n.toString(2)
let b=a.split('0')
let c =b.join("")
let result = c.length
return result
};