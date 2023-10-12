function pickingNumbers(a) {
  // Write your code here
  let maxLengthSub = 0;
  let length = a.length;
  let j = 1;
  let arrCount = Array(101).fill(0);
  for (let i = 0; i <= length - 1; i++) {
    arrCount[a[i]] += 1;
  }
  for (let i = 0; i < arrCount.length - 2; i++) {
    maxLengthSub = Math.max(maxLengthSub, arrCount[i] + arrCount[j]);
    j += 1;
  }
  return maxLengthSub;
}

// const a: number[] = [4, 6, 5, 3, 3, 1];
const a = [1, 2, 2, 3, 1, 2];

console.log(pickingNumbers(a));
