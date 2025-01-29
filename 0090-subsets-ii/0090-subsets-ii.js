/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function(nums) {
        const res = [];
        const curr = [];

        nums.sort((a,b)=>a-b);

        const backtrack = (start) => {
            if (start > nums.length - 1) {
                res.push([...curr]);
                return
            }
   
            curr.push(nums[start]);
            backtrack(start + 1);
            curr.pop();
            while (nums[start] === nums[start + 1]) {
                start++;
            }
            backtrack(start + 1);
        }

        backtrack(0);
        return res;
};