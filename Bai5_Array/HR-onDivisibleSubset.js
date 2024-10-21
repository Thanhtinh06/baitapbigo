const testCase = [1, 7, 2, 4];
const k = 2;

// const testCase = [
//   278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436,
// ];
// const k = 7;

// const testCase = [19, 10, 12, 10, 24, 25, 22];
// const k = 4;

function nonDivisibleSubset(k, array) {
  let simple = new Array(k).fill(0);
  let count = 0;

  array.forEach((item) => {
    simple[item % k]++;
  });
  if (simple[0]) count++;
  if (simple[k / 2]) count++;

  for (let i = 1; i < k / 2; i++) {
    count += Math.max(simple[i], simple[k - i]);
  }

  return count;
}

console.log("result", nonDivisibleSubset(k, testCase));
