var plusOne = (digits) => {
  let total = 0;
  let m = 1;
  let n = digits.length;
  let result = [];

  for (let i = n - 1; i >= 0; i--) {
    total += digits[i] * m;
    m *= 10;
  }
  total += 1;

  while (total > 0) {
    result.push(total % 10);
    total = Math.floor(total / 10);
  }

  return result.reverse();
};
