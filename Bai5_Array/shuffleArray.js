// /**
//  * @param {number[]} nums
//  * @param {number} n
//  * @return {number[]}
//  */
// var shuffle = function(nums, n) {
//   let ans = [];
//   for (let i = 0; i < n; i ++){
//     ans.push(nums[i],nums[n+i])
//   }
//   return ans   
// };

// console.log(shuffle([1,1,2,2],2))


// **
//  * @param {number[]} nums
//  * @param {number} n
//  * @return {number[]}
//  */
var shuffle = function(nums, n) {
  let ans = [];
  let j = 0;
  for (let i = 0; i < 2*n; i += 2){
    ans[i] = nums[j];
    ans[i+1] = nums[n+j];
    j += 1
  }
  return ans   
};
