// /**
//  * @param {string} jewels
//  * @param {string} stones
//  * @return {number}
//  */
// var numJewelsInStones = function(jewels, stones) {
//   let count = 0;
//   for(let char of stones){
//     if(jewels.split("").includes(char)){
//       count += 1
//     }
//   }
//   return count
// };

//cach 2
/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function(jewels, stones) {
  const overlaps = Array.from(stones).filter(stone => jewels.includes(stone));

  return overlaps.length;
};

console.log(numJewelsInStones('Aa','aaaAAABB'))