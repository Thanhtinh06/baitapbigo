/**
 * @param {string} word
 * @return {boolean}
 */
var equalFrequency = function (word) {
  let objFre = {};
  for (char of word) {
    if (objFre[char] !== undefined) {
      objFre[char] += 1;
    } else {
      objFre[char] = 1;
    }
  }
  let lengthObj = Object.keys(objFre).length;
  if (lengthObj === 1) {
    return true;
  }

  let flag;
  let countFlag = 0;
  let term;
  let countTerm = 0;
  let countChange = 0;
  for (key in objFre) {
    if (flag === undefined) {
      flag = objFre[key];
    } else if (flag !== objFre[key] && term !== objFre[key]) {
      term = objFre[key];
      countChange += 1;
      if (countChange > 1) {
        return false;
      }
    }

    if (objFre[key] == flag) {
      countFlag += 1;
    } else {
      countTerm += 1;
    }
  }
  if (countChange == 0) {
    if (flag == 1) {
      return true;
    }
    return false;
  } else {
    if (countTerm == 1 || countFlag == 1) {
      if ((flag == 1 && countFlag == 1) || (term == 1 && countTerm == 1)) {
        return true;
      } else if (Math.abs(flag - term) == 1) {
        if (
          (countFlag == 1 && flag > term) ||
          (countTerm == 1 && flag < term)
        ) {
          return true;
        }
        return false;
      } else {
        return false;
      }
    }
    return false;
  }
};

var result = equalFrequency("aabbbccc");
console.log(result);
