const m = 8;
const arr = [1, 3, 4, 4, 6, 8];

function icecreamParlor(m, arr) {
  // Write your code here
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] + arr[j] === m) {
        return [i + 1, j + 1];
      }
    }
  }
}

console.log("result", icecreamParlor(m, arr));
