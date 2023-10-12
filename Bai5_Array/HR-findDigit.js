function findDigits(n) {
  // Write your code here
  let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
  let count = 0;
  let divisors = [];
  for (let i = 0; i < arr.length; i++) {
    if (n % arr[i] === 0) {
      divisors.push(arr[i]);
    }
  }
  let arrNum = Array.from(`${n}`);
  for (let i = 0; i < arrNum.length; i++) {
    if (divisors.includes(Number(arrNum[i]))) {
      count += 1;
    }
  }
  return count;
}

console.log(findDigits(1012));
