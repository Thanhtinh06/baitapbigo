// const width = 5;
// const height = 1;

// let line = "000.";

// let arr = Array(height)
//   .fill(0)
//   .map((x) => Array(width).fill(0));

// for (let i = 0; i < height; i++) {
//   const line = readline();
//   let newArr = line.split("");
//   newArr.forEach((element, j) => {
//     if (element === "0") {
//       updateGrid(arr, i, j);
//     }
//   });
// }

// function updateGrid(grid, i, j) {
//   grid[i][j] = 1;
// }

const width = 5;
const height = 1;

const arr = [[1, 0, 1, 0, 1]];
// const arr = [
//   [1, 1],
//   [1, 0],
// ];

function findNeighbor(grid) {
  let arr = [];
  for (let i = 0; i < height; i++) {
    for (let j = 0; j < width; j++) {
      if (grid[i][j] === 1) {
        arr.push([j, i]);
      }
    }
  }
  for (let k = 0; k < arr.length; k++) {
    let result = [arr[k][0], arr[k][1], -1, -1, -1, -1];
    for (let m = 0; m < arr.length; m++) {
      if (k !== m) {
        if (arr[k][0] === arr[m][0] && arr[k][1] < arr[m][1]) {
          result[4] = arr[m][0];
          result[5] = arr[m][1];
          break;
        }
      }
      for (let m = 0; m < arr.length; m++) {
        if (k !== m) {
          if (arr[k][1] === arr[m][1] && arr[k][0] < arr[m][0]) {
            result[2] = arr[m][0];
            result[3] = arr[m][1];
            break;
          }
        }
      }
    }
    console.log(result.join(" "));
  }
}

findNeighbor(arr);
