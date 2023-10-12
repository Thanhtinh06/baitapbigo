let sticks = [7, 6, 1, 1, 1, 0];

function maximumPerimeterTriangle(sticks) {
  // Write your code here
  let sortedList = sticks.sort(function (a, b) {
    return a - b;
  });

  let length = sortedList.length;
  for (let i = length - 1; i > 1; i--) {
    if (sortedList[i - 1] + sortedList[i - 2] > sortedList[i]) {
      return sortedList.slice(i - 2, i + 1);
    }
  }
  return [-1];
}
