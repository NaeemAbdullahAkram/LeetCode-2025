/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
  const n = nums.length;
  let minIdxToReachEnd = n-1;
  for(let i=n-2; i>=0; i--) {
    if(nums[i] + i >= minIdxToReachEnd) {
      minIdxToReachEnd = i;
    }
  }
  return minIdxToReachEnd === 0;
};