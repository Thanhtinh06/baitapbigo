function extraLongFactorials(n) {
  // Recursive factorial function
  const factorial = (n) =>
    n === BigInt(0) || n === BigInt(1)
      ? BigInt(1)
      : BigInt(n) * factorial(n - BigInt(1));

  const result = String(factorial(BigInt(n)));

  console.log(result);
}

extraLongFactorials(25);
