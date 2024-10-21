var maxProfit = function (prices) {
  let min = 10 ** 4;
  let maxProfit = 0;

  for (let i = 0; i < prices.length; i++) {
    if (prices[i] < min) {
      min = prices[i];
    } else if (prices[i] - min >= maxProfit) {
      maxProfit = prices[i] - min;
    }
  }
  return maxProfit;
};

maxProfit([2, 4, 1]);
