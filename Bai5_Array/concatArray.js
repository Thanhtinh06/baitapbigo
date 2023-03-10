// /**
//  * @param {number[]} nums
//  * @return {number[]}
//  */
// var getConcatenation = function(nums) {
//     let ans = [...nums];
//     let n = nums.length;
//     for (let i = 0;i < n; i++){
//       ans.push(nums[i])
//     }
//     return ans
// };

//cach2

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
  let ans = []
  let n = nums.length;
  for (let i = 0;i < n; i++){
    ans[i] = nums[i];
    ans[i+n] = nums[i];
  }
  return ans
};
