/**
 * @param {number[]} num
 * @param {number} k
 * @return {number[]}
 */
var addToArrayForm = function(num, k) {
    let numDigit = BigInt('0');
    let count = 1;
    for (let i = 1; i < num.length + 1; i++){
        numDigit += BigInt(num[num.length - i] * count);
        count *= 10
    };
    numDigit += BigInt(`${k}`);
    const number = BigInt('10');
    let arrResult = [];
    for (let i = 1; numDigit > 0; i++){
        let digit = parseInt(numDigit % number);
        numDigit =  BigInt(numDigit/number);
        arrResult.push(digit)
    };
    return arrResult.reverse()
};

console.log(addToArrayForm([1,2,6,3,0,7,1,7,1,9,7,5,6,6,4,4,0,0,6,3],516));