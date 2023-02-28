/**
 * @param {string[]} operations
 * @return {number}
 */
var finalValueAfterOperations = function(operations) {
    let x = 0;
    const incre = ["++X","X++"];
    for(opera of operations){
      if(opera === incre[0] || opera === incre[1]){
        x += 1;
      }else{
        x -=1;
      }
    }
    return x;
};

var operations = ["X++","++X","--X","X--"];
var result = finalValueAfterOperations(operations);
console.log(result)