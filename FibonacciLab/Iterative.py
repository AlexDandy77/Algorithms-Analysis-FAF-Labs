import time
import matplotlib.pyplot as plt
import pandas as pd

def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    input_set = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]
    execution_times = []

    print("\nIterative Fibonacci Execution Times:")
    for n in input_set:
        start_time = time.time()
        fibonacci_iterative(n)
        elapsed_time = time.time() - start_time
        execution_times.append(elapsed_time)

    df = pd.DataFrame([execution_times], columns=input_set)
    print(df.to_string(index=False))

    plt.figure(figsize=(8, 5))
    plt.plot(input_set, execution_times, marker='o', linestyle='-')
    plt.title("Iterative Fibonacci Function")
    plt.xlabel("n-th Fibonacci Term")
    plt.ylabel("Time (s)")
    plt.grid()
    plt.show()
