/**
 * @param {string} address
 * @return {string}
 */
var defangIPaddr = function(address) {
    const symbol = "[.]";
    let result = "";
    for(char of address){
      if(char === "."){
        result += symbol;
      }else{
        result += char
      }
    }
    return result
};

console.log(defangIPaddr("255.100.50.0"))