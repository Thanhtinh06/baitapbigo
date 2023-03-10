/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
  let result = "";
  let word = [];
  for (let i =0; i < s.length; i++){
    if(s[i] !== ' '){
      word.push(s[i]);
    }else{
      word.reverse()
      result += word.reduce((result,char)=>{
        return result += char
      },"");
      result += ' '
      word = []
    }
  }
  word.reverse()
  result += word.reduce((result,char)=>{
    return result += char
  },"");
  return result
};

//toi uu

// /**
//  * @param {string} s
//  * @return {string}
//  */
// var reverseWords = function(s) {
//   let result = "";
//   let word = '';
//   for (let i =0; i < s.length; i++){
//     if(s[i] !== ' '){
//       word += s[i];
//     }else{
//       result += word.split("").reverse().join("");
//       result += ' '
//       word = ''
//     }
//   }
//   result += word.split("").reverse().join("");
//   return result
// };


// cach 3

/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
  return s.split(" ").map(el => el.split("").reverse().join("")).join(" ")
};

console.log(reverseWords("Let's take LeetCode contest"))