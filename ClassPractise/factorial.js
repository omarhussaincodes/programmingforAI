function factorial(num) {
  if (num < 0) console.log("Please pass in positive integer.");
  else if (num === 0) {
    return 1;
  } else {
    let result = 1;
    while (num > 0) {
      result = result * num;
      num--;
    }
    return result;
  }
}

console.log("Result:", factorial(1));
console.log("Result:", factorial(0));
console.log("Result:", factorial(10));
console.log("Result:", factorial(5));
console.log("Result:", factorial(7));
