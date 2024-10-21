s = "Pretty simple";
let answer = 0;

function calculateAsciiSumDividedByLength(inputString) {
  const asciiSum = inputString.split("").reduce((sum, char) => {
    if (char !== "") {
      return sum + char.charCodeAt(0);
    }
  }, 0);
  const result = asciiSum % inputString.length;
  return result;
}

// Example usage:
const inputString = "Pretty simple";
const result = calculateAsciiSumDividedByLength(inputString);
