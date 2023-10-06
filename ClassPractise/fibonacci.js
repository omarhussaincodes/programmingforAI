// Fibonacci Sequence
// 1,1,2,3,5,8,13,21,34

function fibonacci(fib_n_term) {
  if (fib_n_term === 1 || fib_n_term == 2) {
    return 1;
  }

  let count = 0;
  let prev_num = 1;
  let curr_num = 1;
  let sum;

  while (count < fib_n_term) {
    console.log(curr_num);
    sum = prev_num + curr_num;
    prev_num = curr_num;
    curr_num = sum;
    count++;
  }
}

fibonacci(7);
