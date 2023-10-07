# Timing: iterative vs recursive factorial

import time
import sys
sys.setrecursionlimit(1000)

def fact_recursive(n):
    if n == 1:
        return 1
    else:
        return n*fact_recursive(n-1)


start_time = time.time()
fact_recursive(999)
end_time = time.time()
print(f"Elapsed recursive:{end_time-start_time}")
