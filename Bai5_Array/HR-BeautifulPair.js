const testCase1 = {
  A: [6, 5, 4, 3, 2, 1],
  B: [12, 11, 6, 5, 4],
  result: 4,
};
const testCase2 = {
  A: [3, 5, 7, 11, 5, 8],
  B: [5, 7, 11, 10, 5, 8],
  result: 6,
};
const testCase3 = {
  A: [2, 2, 2, 2, 2, 2],
  B: [2, 2, 2, 2, 2, 2],
  result: 5,
};
const testCase4 = {
  A: [2, 2, 6, 1],
  B: [2, 2, 8, 2],
  result: 3,
};

const testCase5 = {
  A: [1],
  B: [1],
  result: 0,
};

function beautifulPairs(A, B) {
  // Write your code here
  let counter = 0;
  for (let i = 0; i < A.length; i++) {
    const INDEX = B.indexOf(A[i]);
    if (INDEX !== -1) {
      counter++;
      B.splice(INDEX, 1);
    }
  }
  return B.length ? counter + 1 : counter - 1;
}

class CallFunc {
  testCase = [testCase1, testCase2, testCase3, testCase4, testCase5];
  callFunc() {
    this.testCase.forEach((value) => {
      const result = beautifulPairs(value.A, value.B);
      if (result === value.result) {
        console.log("Pass");
      } else {
        console.log("Fail");
        console.log("result", result);
      }
    });
  }
}

const call = new CallFunc();
call.callFunc();
