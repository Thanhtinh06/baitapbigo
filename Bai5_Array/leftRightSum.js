/**
 * @param {number[]} nums
 * @return {number[]}
 */
// var leftRigthDifference = function(nums) {
//     let totalArray = 0;
//     let left = 0;
//     let ans = [];

//     nums.forEach(num => totalArray += num)

//     for (let i =0; i < nums.length; i++){
//       let right = totalArray - nums[i] - left
//       ans.push(Math.abs(left-right));
//       left += nums[i]
//     }
//     return ans
// };

//dung ham co san JS

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var leftRigthDifference = function (nums) {
  let totalArray = nums.reduce((totalArray, num) => {
    return (totalArray += num);
  }, 0);
  let left = 0;
  let ans = [];

  for (let i = 0; i < nums.length; i++) {
    let right = totalArray - nums[i] - left;
    ans.push(Math.abs(left - right));
    left += nums[i];
  }
  return ans;
};

console.log(leftRigthDifference([10, 4, 8, 3]));
