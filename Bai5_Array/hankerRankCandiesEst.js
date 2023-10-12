// let arr = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1];

// let arr = [4, 5, 6, 7, 4, 3, 2, 1];
// // let arr = [2, 4, 3, 5, 2, 6, 4, 5];
// // let arr = [3, 4, 7, 8, 8, 8, 4, 3, 7, 2];
// let arr = [1, 1, 1, 1, 1, 1];
// let arr = [5, 4, 3, 2, 1]; // 15

// let arr = [
//   6, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 2, 2, 1, 1, 2, 3, 4, 5, 12, 4,
//   5, 6, 13, 413, 4, 412, 24, 5, 2, 1, 4, 6, 7, 9,
// ];
// let arr = [
//   3, 2, 1, 1, 2, 3, 2, 2, 1, 1, 2, 3, 4, 5, 12, 4, 5, 6, 13, 413, 4, 412, 24, 5,
//   2, 1, 4, 6, 7, 9,
// ];

let arr = [
  54276, 12221, 12221, 67417, 12279, 12279, 5811, 88620, 88620, 16895, 87385,
  62745, 62745, 61929, 59941, 72016, 72016, 24921,
];

let n = arr.length;
function candies(n, arr) {
  // Write your code here
  let newArr = [0, ...arr, 10 ** 5 + 1];
  let candiesList = Array(n + 2).fill(1);
  candiesList[0] = newArr[1] > newArr[2] ? 1 : 0;
  candiesList[n + 1] = 0;

  for (let i = 1; i < n + 1; i++) {
    if (newArr[i] > newArr[i - 1] && newArr[i] <= newArr[i + 1]) {
      candiesList[i] += candiesList[i - 1];
    } else if (
      (newArr[i] < newArr[i - 1] || newArr[i] >= newArr[i - 1]) &&
      newArr[i] > newArr[i + 1]
    ) {
      if (newArr[i] > newArr[i - 1]) {
        candiesList[i] += candiesList[i - 1];
      }
      let j = i;
      let countNeed = 0;
      while (j <= n + 1) {
        if (newArr[j] <= newArr[j + 1]) {
          break;
        }
        countNeed += 1;
        j += 1;
      }
      countNeed += 1;
      while (i < j + 1) {
        if (candiesList[i] < countNeed) {
          candiesList[i] = countNeed;
        }
        countNeed -= 1;
        i += 1;
      }
      i -= 1;
    }
  }
  let result = candiesList.reduce((a, b) => {
    return a + b;
  }, -candiesList[0]);
  return result;
}

console.log("lisr", candies(n, arr));
